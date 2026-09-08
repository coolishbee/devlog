"""빌드 결과의 언어 연결과 저장소 하위 경로, 로컬 파일 참조를 검증합니다."""

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.ids = set()
        self.language = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.language = attrs.get('lang')
        if 'id' in attrs:
            self.ids.add(attrs['id'])
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
    base_url = args.base_url or re.search(r'^baseURL:\s*(\S+)', Path('hugo.yaml').read_text(), re.M)[1]
    base_url = base_url.rstrip('/') + '/'
    base = urlsplit(base_url)
    output = Path(args.directory)
    errors = set()
    pages = {}

    def require(condition, message):
        if not condition:
            errors.add(message)

    require(output.is_dir(), '빌드 결과가 없습니다. 먼저 사이트를 빌드하세요.')
    for path in output.rglob('*.html'):
        pages[path] = Page(path.read_text())

    def check_reference(reference, owner):
        if reference.startswith(('#', 'data:', 'mailto:', 'tel:', 'javascript:')):
            return
        address = urlsplit(urljoin(base_url + owner.relative_to(output).as_posix(), reference))
        if address.scheme not in ('http', 'https') or address.netloc != base.netloc:
            return
        prefix = base.path.rstrip('/')
        path = unquote(address.path)
        if path != prefix and not path.startswith(prefix + '/'):
            errors.add(f'{owner}: 배포 경로를 벗어난 참조 {reference}')
            return
        target = output / path[len(prefix):].lstrip('/')
        if target.is_dir():
            target = target / 'index.html'
        require(target.is_file(), f'{owner}: 파일을 찾을 수 없는 참조 {reference}')

    for owner, page in pages.items():
        for reference in page.references:
            check_reference(reference, owner)
    for owner in output.rglob('*.css'):
        for reference in re.findall(r'url\([\s\"\']*([^\)\"\']+)', owner.read_text()):
            check_reference(reference, owner)

    for language, prefix in [('en', ''), ('ko', 'ko/')]:
        home = output / prefix / 'index.html'
        require(home in pages, f'{language}: 홈 화면 누락')
        if home in pages:
            require((pages[home].language or '').split('-')[0] == language, f'{language}: 문서 언어 설정 오류')
            for section in ['home', 'about', 'skills', 'experiences', 'education', 'projects', 'publications', 'featured-posts', 'recent-posts', 'accomplishments', 'achievements']:
                require(section in pages[home].ids, f'{language}: 홈 영역 누락 {section}')
        for required in ['posts/index.html', 'notes/index.html', 'search/index.html', 'index.json', 'index.xml', '404.html', 'sitemap.xml']:
            require((output / prefix / required).is_file(), f'{language}: 필수 결과 누락 {required}')
        index_file = output / prefix / 'index.json'
        if index_file.is_file():
            entries = json.loads(index_file.read_text())
            require(bool(entries), f'{language}: 검색 색인이 비어 있음')
            for entry in entries:
                require(entry['permalink'].startswith(base_url + prefix), f'{language}: 검색 결과의 언어 경로 오류')
                if language == 'en':
                    require(not entry['permalink'].startswith(base_url + 'ko/'), '영어 색인에 한국어 글이 포함됨')
                check_reference(entry['permalink'], home)
                if entry.get('hero'):
                    check_reference(entry['hero'], home)

    sources = [p for p in Path('content').rglob('*.md') if not p.name.endswith('.ko.md')]
    for english in sources:
        korean = english.with_name(english.stem + '.ko.md')
        require(korean.is_file(), f'한국어 번역 누락: {english}')
        if english.name != 'index.md':
            continue
        route = english.parent.relative_to('content').as_posix() + '/'
        for prefix, other in [('', 'ko/'), ('ko/', '')]:
            page_path = output / prefix / route / 'index.html'
            require(page_path in pages, f'콘텐츠 페이지 누락: {page_path}')
            if page_path in pages:
                expected = base.path + other + route
                paths = [urlsplit(urljoin(base_url, ref)).path for ref in pages[page_path].references]
                require(expected in paths, f'대응 언어 페이지 연결 누락: {page_path}')

    for language in ['bn', 'fr', 'de', 'es']:
        require(not (output / language).exists(), f'불필요한 언어 경로 생성: {language}')
    if errors:
        print('\n'.join(sorted(errors)), file=sys.stderr)
        return 1
    print(f'검증 완료: 문서 {len(pages)}개, 번역 쌍 {len(sources)}개, 영어·한국어 검색 색인과 로컬 참조가 정상입니다.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
