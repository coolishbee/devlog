---
title: "단축 코드 예제"
date: 2020-06-08T08:06:25+06:00
description: 단축 코드의 다양한 기능을 확인하는 예제입니다.
menu:
  sidebar:
    name: 단축 코드 예제
    identifier: shortcodes
    weight: 40
hero: boat.jpg
mermaid: true
---

이 글은 다음 기능을 확인하기 위한 예제입니다.

- 대표 이미지 표시
- 다양한 단축 코드

## 알림

이 테마에서는 다음과 같은 알림을 사용할 수 있습니다.

{{< alert type="success" >}}
다음 속성을 사용하는 알림 예제입니다: `type="success"`.
{{< /alert >}}

{{< alert type="danger" >}}
다음 속성을 사용하는 알림 예제입니다: `type="danger"`.
{{< /alert >}}

{{< alert type="warning" >}}
다음 속성을 사용하는 알림 예제입니다: `type="warning"`.
{{< /alert >}}

{{< alert type="info" >}}
다음 속성을 사용하는 알림 예제입니다: `type="info"`.
{{< /alert >}}

{{< alert type="dark" >}}
다음 속성을 사용하는 알림 예제입니다: `type="dark"`.
{{< /alert >}}

{{< alert type="primary" >}}
다음 속성을 사용하는 알림 예제입니다: `type="primary"`.
{{< /alert >}}

{{< alert type="secondary" >}}
다음 속성을 사용하는 알림 예제입니다: `type="secondary"`.
{{< /alert >}}

## 이미지

#### 크기나 정렬 속성을 지정하지 않은 이미지

{{< img src="/posts/shortcodes/boat.jpg" title="바다 위의 배" >}}

{{< vs 3 >}}

#### `height`와 `width` 속성을 지정한 이미지

{{< img src="/posts/shortcodes/boat.jpg" height="400" width="600" title="바다 위의 배" >}}

{{< vs 3 >}}

#### `height`와 `width` 속성을 지정하고 가운데 정렬한 이미지

{{< img src="/posts/shortcodes/boat.jpg" height="400" width="600" align="center" title="바다 위의 배" >}}

{{< vs 3 >}}

#### `float` 속성을 지정한 이미지

{{< img src="/posts/shortcodes/boat.jpg" height="200" width="500" float="right" title="바다 위의 배" >}}

이 문단은 이미지 옆으로 본문이 흐르는 모습을 확인하기 위한 예제입니다. 이미지를 오른쪽에 배치하면 글이 남은 공간을 따라 표시됩니다. 문장이 길어져 이미지의 아래쪽까지 이어지면 본문은 다시 전체 너비를 사용합니다. 화면 크기에 따라 줄바꿈과 여백이 어떻게 달라지는지 살펴보세요. 작은 화면에서도 이미지와 글이 겹치지 않고 읽기 편하게 배치되는지 확인할 수 있습니다.

두 번째 문단에서도 이미지와 본문의 관계를 살펴볼 수 있습니다. 이미지의 크기와 배치를 조절하여 글의 내용을 더 잘 전달해 보세요. 이 문장은 문단 사이의 간격과 자연스러운 흐름을 보여주기 위한 예제입니다.

## 열 나누기

이 테마에서는 페이지를 원하는 수의 열로 나눌 수 있습니다.

#### 두 개의 열

{{< split 6 6>}}

##### 왼쪽 열

왼쪽 열에 들어가는 예제 문단입니다. 각 열에는 제목, 본문, 이미지 등 다양한 내용을 배치할 수 있습니다.

---

##### 오른쪽 열

오른쪽 열에 들어가는 예제 문단입니다. 여러 내용을 나란히 놓아 비교하거나 관련 정보를 함께 보여줄 수 있습니다.

{{< /split >}}

#### 세 개의 열

{{< split 4 4 4 >}}

##### 왼쪽 열

왼쪽 열에 들어가는 예제 문단입니다. 각 열에는 제목, 본문, 이미지 등 다양한 내용을 배치할 수 있습니다.

---

##### 가운데 열

가운데 열에 들어가는 예제 문단입니다. 화면 크기에 따른 열의 배치를 확인해 보세요.

---

##### 오른쪽 열

오른쪽 열에 들어가는 예제 문단입니다. 여러 내용을 나란히 놓아 비교하거나 관련 정보를 함께 보여줄 수 있습니다.

{{< /split >}}

## 세로 여백

두 줄 사이에 세로 여백을 추가합니다.

첫 번째 줄입니다.
{{< vs 4>}}
두 번째 줄입니다. 이전 줄과의 사이에 `4rem`의 세로 여백이 생깁니다.

## 동영상

{{< video src="/videos/sample.mp4" >}}

<!-- markdown-link-check-disable-next-line -->
영상은 [펙셀스](https://www.pexels.com)의 [라훌 샤르마](https://www.pexels.com/@rahul-sharma-493988)가 제공합니다.

## 도표

다음은 도표 단축 코드의 사용 예제입니다.

**흐름도:**

{{< mermaid align="left" >}}
graph LR;
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
{{< /mermaid >}}

**순서도:**

{{< mermaid >}}
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
{{< /mermaid >}}

**간트 차트:**

{{< mermaid >}}
gantt
  dateFormat  YYYY-MM-DD
  title Adding GANTT diagram to mermaid
  excludes weekdays 2014-01-10

section A section
  Completed task            :done,    des1, 2014-01-06,2014-01-08
  Active task               :active,  des2, 2014-01-09, 3d
  Future task               :         des3, after des2, 5d
  Future task2               :         des4, after des3, 5d
{{< /mermaid >}}

**클래스 다이어그램:**

{{< mermaid >}}
classDiagram
  Class01 <|-- AveryLongClass : Cool
  Class03 *-- Class04
  Class05 o-- Class06
  Class07 .. Class08
  Class09 --> C2 : Where am i?
  Class09 --* C3
  Class09 --|> Class07
  Class07 : equals()
  Class07 : Object[] elementData
  Class01 : size()
  Class01 : int chimp
  Class01 : int gorilla
  Class08 <--> C2: Cool label
{{< /mermaid >}}

**깃 그래프:**

{{< mermaid >}}
gitGraph
    commit id: "ZERO"
    branch develop
    commit id:"A"
    checkout main
    commit id:"ONE"
    checkout develop
    commit id:"B"
    checkout main
    commit id:"TWO"
    cherry-pick id:"A"
    commit id:"THREE"
    checkout develop
    commit id:"C"
{{< /mermaid >}}

**개체 관계도:**

{{< mermaid >}}
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
{{< /mermaid >}}

## 외부 코드 조각

{{< gist hossainemruz 4ad86c9b6378677e14eff12713e75e44 >}}

## 문서 삽입

{{< embed-pdf src="/files/resume.pdf" >}}
