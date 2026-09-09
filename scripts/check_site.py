"""한국어 전용 사이트의 콘텐츠, 검색 색인, 배포 경로와 문서 앵커를 검증합니다."""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.ids = set()
        self.language = None
        self.alternate_languages = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.language = attrs.get('lang')
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if attrs.get('hreflang'):
            self.alternate_languages.add(attrs['hreflang'])
        for name in ('href', 'src', 'action', 'poster', 'data-url', 'data-index'):
            if attrs.get(name):
                self.references.append(attrs[name])
        for value in re.findall(r'url\([\s\"\']*([^\)\"\']+)', attrs.get('style', '')):
            self.references.append(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', default='public')
    parser.add_argument('--base-url')
    args = parser.parse_args()
    config = Path('hugo.yaml').read_text()
    base_url = args.base_url or re.search(r'^baseURL:\s*(\S+)', config, re.M)[1]
    base_url = base_url.rstrip('/') + '/'
    base = urlsplit(base_url)
    output = Path(args.directory)
    errors = set()

    def require(condition, message):
        if not condition:
            errors.add(message)

    require(output.is_dir(), '빌드 결과가 없습니다. 먼저 사이트를 빌드하세요.')
    require(bool(re.search(r'^defaultContentLanguage:\s*ko\s*$', config, re.M)), '기본 언어는 한국어여야 합니다.')
    language_block = re.search(r'^languages:\n((?:[ \t].*\n|\n)*)', config, re.M)
    languages = re.findall(r'^  ([\w-]+):', language_block[1], re.M) if language_block else []
    require(languages == ['ko'], '사이트 언어 설정에는 한국어만 있어야 합니다.')
    for source in ['data/en', 'i18n/en.toml', 'layouts/partials/navigators/lang-selector.html']:
        require(not Path(source).exists(), f'다국어 전용 파일이 남아 있습니다: {source}')

    pages = {path: Page(path.read_text()) for path in output.rglob('*.html')}
    prefix = base.path.rstrip('/')

    def check_reference(reference, owner):
        original = urlsplit(reference)
        address = urlsplit(urljoin(base_url + owner.relative_to(output).as_posix(), reference))
        if address.scheme not in ('http', 'https') or address.netloc != base.netloc:
            return
        path = unquote(address.path)
        if path != prefix and not path.startswith(prefix + '/'):
            if original.scheme in ('http', 'https') and original.netloc:
                return
            errors.add(f'{owner}: 배포 경로를 벗어난 참조 {reference}')
            return
        relative = path[len(prefix):].lstrip('/')
        require(not relative.startswith(('en/', 'ko/')), f'{owner}: 언어별 경로 참조 {reference}')
        target = output / relative
        if target.is_dir():
            target /= 'index.html'
        require(target.is_file(), f'{owner}: 파일을 찾을 수 없는 참조 {reference}')
        if address.fragment and target in pages:
            require(unquote(address.fragment) in pages[target].ids, f'{owner}: 문서 앵커를 찾을 수 없는 참조 {reference}')

    for owner, page in pages.items():
        require((page.language or '').split('-')[0] == 'ko', f'{owner}: 문서 언어가 한국어가 아닙니다.')
        require('languageSelector' not in page.ids, f'{owner}: 언어 선택 메뉴가 남아 있습니다.')
        require(all(lang.split('-')[0] == 'ko' for lang in page.alternate_languages), f'{owner}: 다른 언어 페이지 연결이 남아 있습니다.')
        for reference in page.references:
            check_reference(reference, owner)
    for owner in output.rglob('*.css'):
        for reference in re.findall(r'url\([\s\"\']*([^\)\"\']+)', owner.read_text()):
            check_reference(reference, owner)

    home = output / 'index.html'
    require(home in pages, '홈 화면이 없습니다.')
    if home in pages:
        for section in ['home', 'about', 'skills', 'experiences', 'education', 'projects', 'publications', 'featured-posts', 'recent-posts', 'accomplishments', 'achievements']:
            require(section in pages[home].ids, f'홈 영역 누락: {section}')
    for required in ['posts/index.html', 'notes/index.html', 'search/index.html', 'index.json', 'index.xml', '404.html', 'sitemap.xml', 'robots.txt']:
        require((output / required).is_file(), f'필수 결과 누락: {required}')

    markdown = list(Path('content').rglob('*.md'))
    post_urls = set()
    for source in markdown:
        require(source.name.endswith('.ko.md'), f'한국어 이외의 콘텐츠 파일: {source}')
        if source.name not in ('index.ko.md', '_index.ko.md'):
            continue
        route = source.parent.relative_to('content').as_posix() + '/'
        require((output / route / 'index.html') in pages, f'콘텐츠 페이지 누락: {source}')
        if source.name == 'index.ko.md' and route.startswith('posts/'):
            post_urls.add(base_url + route)

    index_file = output / 'index.json'
    if index_file.is_file():
        entries = json.loads(index_file.read_text())
        require(bool(entries), '검색 색인이 비어 있습니다.')
        urls = {entry['permalink'] for entry in entries}
        for url in sorted(post_urls - urls):
            errors.add(f'게시글 검색 색인 누락: {url}')
        for entry in entries:
            require(entry['permalink'].startswith(base_url), '검색 결과의 배포 경로 오류')
            require(bool(re.search(r'\d+년\s*\d+월\s*\d+일', entry.get('date', ''))), f"한국어 검색 날짜 표시 오류: {entry['permalink']}")
            check_reference(entry['permalink'], home)
            if entry.get('hero'):
                check_reference(entry['hero'], home)

    sitemap_urls = set()
    for owner in output.rglob('*.xml'):
        try:
            tree = ET.parse(owner)
        except ET.ParseError as error:
            errors.add(f'{owner}: 올바르지 않은 XML 문서: {error}')
            continue
        for node in tree.iter():
            tag = node.tag.rsplit('}', 1)[-1]
            if tag in ('loc', 'link') and node.text and node.text.strip().startswith(('http://', 'https://')):
                check_reference(node.text.strip(), owner)
                if tag == 'loc':
                    sitemap_urls.add(node.text.strip())
            if node.attrib.get('href'):
                check_reference(node.attrib['href'], owner)
            if node.attrib.get('hreflang'):
                require(node.attrib['hreflang'].split('-')[0] == 'ko', f'{owner}: 다른 언어의 사이트맵 연결이 남아 있습니다.')
    for url in sorted(post_urls - sitemap_urls):
        errors.add(f'게시글 사이트맵 누락: {url}')

    for language in ['en', 'ko', 'bn', 'fr', 'de', 'es']:
        require(not (output / language).exists(), f'불필요한 언어 경로 생성: {language}')
    require(not Path('content/posts/project/python-lunch').exists(), '제외 대상인 점심 메뉴 글이 포함되어 있습니다.')
    if errors:
        print('\n'.join(sorted(errors)), file=sys.stderr)
        return 1
    print(f'검증 완료: 한국어 문서 {len(pages)}개, 게시글 {len(post_urls)}개, 검색 색인·사이트맵·로컬 참조·문서 앵커가 정상입니다.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
