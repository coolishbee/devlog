# Repository Guidelines

## 프로젝트 구조와 모듈 구성

이 저장소는 Toha 테마를 Hugo 모듈로 사용하는 한국어·영어 개발 블로그다. 글과 노트는 `content/`에 두고, 영어 `index.en.md`와 한국어 `index.ko.md`를 같은 번들 디렉터리에 유지한다. 홈 화면 데이터는 `data/en/`과 `data/ko/`, 번역 문자열은 `i18n/`에 있다. 테마 덮어쓰기는 `layouts/`, 브라우저 코드와 스타일·가공 이미지는 `assets/`, 그대로 배포할 파일은 `static/`에 둔다. 빌드 검증기는 `scripts/check_site.py`, 자동 배포 설정은 `.github/workflows/deploy.yml`에 있다. 생성되는 `public/`, `resources/`, `node_modules/`는 커밋하지 않는다.

## 빌드, 검증, 개발 명령

- `mise install`: `mise.toml`에 고정된 Hugo Extended, Go, Node.js를 설치한다.
- `mise exec -- npm ci --include=dev`: 잠금 파일과 일치하는 의존성을 설치한다.
- `mise exec -- npm run dev`: 로컬 서버를 `http://localhost:1313/devlog/`에서 실행한다.
- `mise exec -- npm run build`: 배포용 사이트를 정리하고 최소화해 `public/`에 생성한다.
- `npm run check`: 빌드 결과의 링크, 필수 페이지, 검색 색인, 번역 연결을 검사한다. 먼저 빌드해야 한다.

## 코딩 스타일과 이름 규칙

기존 파일의 형식을 따른다. JavaScript와 SCSS는 2칸 들여쓰기, JavaScript는 세미콜론 없이 Standard 스타일을 사용한다. Python은 4칸 들여쓰기와 `snake_case`를 따른다. 콘텐츠 디렉터리와 식별자는 `lowercase-kebab-case`로 작성한다. 영어 콘텐츠는 `.en.md`, 한국어 번역본은 `.ko.md`로 만들고, 두 파일의 `menu.sidebar.identifier`를 동일하게 유지한다. 템플릿에서는 하위 경로 배포를 깨뜨리는 루트 고정 주소 대신 기존 URL 도우미를 재사용한다.

## 테스트 지침

별도 단위 테스트 프레임워크나 수치형 커버리지 기준은 없다. 변경마다 `npm run build && npm run check`를 실행한다. 화면 변경은 영어·한국어 홈, 모바일 화면, 언어 전환, 검색을 로컬에서 확인한다. 검증기를 수정할 때는 실패 조건에 구체적인 한국어 오류 메시지를 추가한다.

## 커밋과 변경 제안 지침

최근 기록은 짧은 요약형 제목과 `feat:`, `fix:` 접두사를 함께 사용한다. 새 커밋도 한 가지 논리적 변경으로 제한하고, 예를 들어 `feat: 검색 결과 필터 추가`처럼 명령형으로 작성한다. 변경 제안에는 목적, 주요 파일, 실행한 검증 명령을 적고 관련 이슈를 연결한다. 시각 변경에는 영어·한국어 및 필요한 반응형 화면의 캡처를 첨부한다. 설정이나 배포 경로 변경은 영향 범위와 되돌리는 방법도 설명한다.

## 구성과 보안

`hugo.yaml`의 `baseURL`을 바꾸면 언어별 공유 주소도 함께 갱신한다. 개인 토큰이나 실제 비밀값은 커밋하지 말고, 외부 서비스는 필요한 저장소 비밀로 주입한다. 테마 버전을 변경하면 `go.mod`, `go.sum`, 잠금 파일과 전체 빌드 결과를 함께 검증한다.
