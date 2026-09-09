# 개발 블로그

Hugo 정적 사이트 생성기와 Toha 테마로 만든 한국어·영어 개발 블로그입니다.

## 기술 구성

- `Hugo Extended 0.163.3`
- `Toha 4.16.0`
- `Go 1.25`
- `Node.js 22`

## 사용 방법

도구와 의존성을 설치합니다.

```bash
mise install
mise exec -- npm ci --include=dev
```

로컬 개발 서버를 실행합니다.

```bash
mise exec -- npm run dev
```

한국어 사이트는 `http://localhost:1313/devlog/`, 영어 사이트는 `http://localhost:1313/devlog/en/`에서 확인할 수 있습니다.

배포 결과를 만들고 링크와 다국어 구성을 검증합니다.

```bash
mise exec -- npm run build
npm run check
```
