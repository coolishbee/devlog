# 개인 포트폴리오와 개발 블로그

[공식 예제 사이트](https://toha-example-site.netlify.app/)를 기반으로 만든 영어·한국어 사이트입니다. 배경과 이미지, 예제 인물과 경력, 홈의 전체 영역, 글 4개와 노트 5개를 유지했습니다. 영어를 기본으로 제공하며 한국어에서는 홈과 글·노트의 설명까지 번역합니다.

- [영어 사이트](https://coolishbee.github.io/devlog/)
- [한국어 사이트](https://coolishbee.github.io/devlog/ko/)
- [자동 빌드와 배포 기록](https://github.com/coolishbee/devlog/actions/workflows/deploy.yml)
- [공식 사용 가이드](https://toha-docs.netlify.app/posts/)

## 설치와 로컬 실행

필요한 도구는 `Hugo Extended 0.163.3`, `Go 1.25.x`, `Node.js 22.x`, `Python 3.9` 이상입니다. 확장판이 있어야 테마의 스타일을 컴파일할 수 있습니다. 버전 관리 도구인 `mise`를 사용하면 저장소의 `mise.toml`에 맞춰 설치할 수 있습니다.

```bash
mise install
mise exec -- npm ci --include=dev
mise exec -- npm run dev
```

로컬 주소는 `http://localhost:1313/devlog/`이며 한국어는 그 아래의 `ko/`에서 확인합니다. 도구가 이미 실행 경로에 설치되어 있다면 명령 앞의 `mise exec --`를 생략할 수 있습니다.

배포 결과를 만들고 링크와 번역 연결을 확인합니다.

```bash
mise exec -- npm run build
npm run check
```

검증은 생성된 문서와 스타일의 로컬 파일 참조, 언어별 홈 영역, 글·노트의 번역 연결, 검색 색인과 필수 페이지를 확인합니다. 빌드 결과인 `public/`과 의존성·캐시는 커밋하지 않습니다.

## 프로필과 화면 수정

| 수정할 내용 | 위치 |
| --- | --- |
| 배포 주소, 언어, 기능 설정 | `hugo.yaml` |
| 영어 이름·소개·연락처 | `data/en/author.yaml` |
| 한국어 이름·소개·연락처 | `data/ko/author.yaml` |
| 사이트 설명과 문서 메뉴 | 각 언어의 `site.yaml` |
| 기술·경력·학력·프로젝트·수상 정보 | 각 언어의 `sections/` |
| 배경·프로필·카드 이미지 | `assets/images/` |
| 이력서와 영상 | `static/files/`, `static/videos/` |
| 메뉴와 버튼의 한국어 표현 | `i18n/ko.toml` |

홈 영역의 `enable`로 표시 여부, `weight`로 순서, `showOnNavbar`로 메뉴 표시를 조절합니다. 영역의 `id`, 필터와 태그 값은 서로 연결되어 있으므로 관련 값을 함께 수정합니다.

예제의 인물·연락처·외부 링크는 샘플입니다. 개인 사이트로 전환할 때 두 언어의 정보를 함께 교체하세요. 방문 통계, 댓글, 후원, 뉴스레터는 별도의 계정 연결 없이 동작하도록 비활성화했습니다.

## 글과 노트 작성

글은 페이지별 폴더에 영어 원문과 한국어 번역을 나란히 둡니다. 이미지도 같은 폴더에 넣을 수 있습니다.

```text
content/posts/my-post/
  index.md
  index.ko.md
  hero.jpg
```

기존 글의 머리말을 복사하여 제목·설명·날짜를 수정합니다. 두 언어에서 같은 폴더와 메뉴 식별자를 사용하면 서로 대응하는 페이지로 연결됩니다. 예를 들어 영어 원문에는 다음과 같이 설정할 수 있습니다.

```yaml
---
title: "My new post"
date: 2026-09-09T09:00:00+09:00
description: "A short introduction to this post."
hero: hero.jpg
menu:
  sidebar:
    name: "My new post"
    identifier: my-post
    weight: 50
---
```

한국어 파일에서는 제목·설명·메뉴 이름과 본문을 번역하고 `identifier`는 유지합니다. 분류의 소개 페이지도 `_index.md`와 `_index.ko.md`를 함께 작성합니다. 노트는 `content/notes/`의 기존 예제를 복사하여 같은 방식으로 추가합니다. 단축 코드와 수식·도표의 작성법은 공식 가이드를 참고하세요.

## 자동 배포

저장소 설정의 페이지 메뉴에서 게시 소스를 `GitHub Actions`로 지정합니다. 이후 `main`에 변경을 반영하면 빌드와 검증을 거쳐 자동 배포됩니다. 실행 화면에서 해당 브랜치를 선택해 수동으로 배포할 수도 있습니다.

변경 제안에서는 빌드와 검증만 실행합니다. 배포 권한은 게시 작업에만 부여하며, 별도의 개인 배포 토큰 없이 기본 제공 인증을 사용합니다. 실제 공개 주소는 배포 작업과 저장소의 배포 환경에서 확인할 수 있습니다.

배포 주소를 바꾸면 `hugo.yaml`의 `baseURL`과 두 언어의 `site.yaml`에 있는 공유 주소를 함께 수정합니다. 저장소 이름이 붙는 경로와 마지막 `/`까지 포함해야 합니다.

## 원본과 유지보수

테마는 `Toha v4.16.0`으로 고정했습니다. 콘텐츠와 이미지는 [공식 예제 저장소의 기준 커밋](https://github.com/hugo-themes/toha-example-site/tree/905313cb4a508bf05a916003c621816c0d064bca)에서 가져왔으며 원본 라이선스와 저작권 표기를 `LICENSE`에 보존합니다.

저장소 하위 경로에서 동작하도록 언어 전환·글 카드·국기·이미지·영상·문서 삽입의 주소 처리를 보완했습니다. 한국어 검색과 화면 선택·코드 복사 안내도 추가했습니다. 테마 본체는 모듈로 사용하고 필요한 수정만 이 저장소의 템플릿과 스크립트에서 덮어씁니다.

테마를 갱신할 때에는 버전을 명시하여 의존성을 다시 정리한 뒤 잠금 파일과 화면을 함께 검증하세요. 자동으로 테마를 최신 버전으로 바꾸는 작업은 설정하지 않았습니다. 예제의 외부 영상과 소셜 게시물은 원본 서비스의 공개 상태에 따라 표시됩니다.
