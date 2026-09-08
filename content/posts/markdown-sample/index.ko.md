---
title: "마크다운 예제"
date: 2020-06-08T08:06:25+06:00
description: 마크다운 표시 기능을 확인하는 예제입니다.
menu:
  sidebar:
    name: 마크다운 예제
    identifier: markdown
    weight: 30
author:
  name: 제시카 조너스
  image: /images/author/jessica.png
math: true
---

이 글은 다음 기능을 확인하기 위한 예제입니다.

- 사이트의 기본 작성자와 다른 글 작성자
- 목차
- 마크다운 본문 표시
- 수식 표시
- 이모지 표시

---
# 마크다운 문법 표시

## 제목

다음 `<h1>`부터 `<h6>`까지의 요소는 여섯 단계의 제목을 나타냅니다. `<h1>`이 가장 높은 단계이고 `<h6>`이 가장 낮은 단계입니다.

# 제목 1
## 제목 2
### 제목 3
#### 제목 4
##### 제목 5
###### 제목 6

## 문단

이 문단은 본문 글꼴과 줄 간격을 확인하기 위한 한국어 예제입니다. 긴 글을 작성하면 화면의 너비에 맞춰 문장이 자연스럽게 다음 줄로 이어집니다. 글의 내용은 여러 문장으로 구성할 수 있으며, 한 문단 안에서 서로 관련된 생각을 차례로 설명하면 읽기 쉽습니다. 데스크톱에서는 넓은 본문 영역을 활용하고 모바일에서는 작은 화면에 맞는 줄바꿈을 확인할 수 있습니다. 제목과 문단 사이의 여백, 문장의 길이, 강조 표현이 어떻게 보이는지도 함께 살펴보세요. 이 예제는 특정한 사실을 설명하기보다 다양한 길이의 문장이 화면에 표시되는 모습을 보여줍니다.

새 문단을 시작하면 앞 문단과 구분되는 여백이 생깁니다. 짧은 문단과 긴 문단을 함께 배치하여 본문의 읽기 편한 흐름과 정렬 상태를 확인할 수 있습니다.

## 인용문

인용문은 다른 출처에서 가져온 내용을 나타냅니다. 출처는 `footer` 또는 `cite` 요소로 표시할 수 있으며, 본문 안에 주석이나 약어를 덧붙일 수도 있습니다.

#### 출처가 없는 인용문

> 이 문장은 인용문 표시를 확인하기 위한 예제입니다.
> 인용문 안에서도 *마크다운 문법*을 사용할 수 있다는 점을 **확인하세요**.

#### 출처가 있는 인용문

> 메모리를 공유해서 통신하지 말고, 통신을 통해 메모리를 공유하세요.
> — <cite>롭 파이크[^1]</cite>


[^1]: 위 인용문은 2015년 11월 18일 고퍼페스트에서 진행한 롭 파이크의 [발표](https://www.youtube.com/watch?v=PAAkCSZUG1c)에서 가져왔습니다.

## 표

표는 마크다운의 기본 명세에 포함되어 있지 않지만 휴고는 별도 설정 없이 지원합니다.

   | 이름  | 나이 |
   | ----- | --- |
   | 밥    | 27  |
   | 앨리스 | 23  |

#### 표 안의 마크다운

| 표 안에서&nbsp;&nbsp;&nbsp; | 마크다운을&nbsp;&nbsp;&nbsp; | 사용하는&nbsp;&nbsp;&nbsp;                | 예제  |
| ------------------------ | -------------------------- | ----------------------------------- | ------ |
| *기울임*                | **굵게**                   | ~~취소선~~&nbsp;&nbsp;&nbsp; | `code` |

## 코드 블록

#### 백틱으로 감싼 코드 블록

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
```
#### 공백 네 칸으로 들여쓴 코드 블록

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Example HTML5 Document</title>
    </head>
    <body>
      <p>Test</p>
    </body>
    </html>

#### 휴고의 구문 강조 기능을 사용하는 코드 블록
{{< highlight html >}}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
{{< /highlight >}}

## 목록의 종류

#### 순서 있는 목록

1. 첫 번째 항목
2. 두 번째 항목
3. 세 번째 항목

#### 순서 없는 목록

* 목록 항목
* 다른 항목
* 또 다른 항목

#### 중첩 목록

* 과일
  * 사과
  * 오렌지
  * 바나나
* 유제품
  * 우유
  * 치즈

## 그 밖의 요소

<abbr title="그래픽 교환 형식">GIF</abbr>는 비트맵 이미지 형식입니다.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

세션을 종료하려면 <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd>를 누르세요.

대부분의 <mark>도롱뇽</mark>은 야행성이며 곤충, 벌레와 작은 생물을 사냥합니다.

---

## 수식 표시

{{< math.inline >}}
<p>
문장 안의 수식: \(\varphi = \dfrac{1+\sqrt5}{2}= 1.6180339887…\)
</p>
{{</ math.inline >}}

독립된 수식:
$$
 \varphi = 1+\frac{1} {1+\frac{1} {1+\frac{1} {1+\cdots} } }
$$

---

## 이모지 표시

<p><span class="nowrap"><span class="emojify">🙈</span> <code>:see_no_evil:</code></span>  <span class="nowrap"><span class="emojify">🙉</span> <code>:hear_no_evil:</code></span>  <span class="nowrap"><span class="emojify">🙊</span> <code>:speak_no_evil:</code></span></p>
<br>
