---
title: "앱을 포함한 라이브러리 프로젝트 생성"
date: "2023-01-16T01:56:38+09:00"
lastmod: "2023-01-16T01:56:38+09:00"
tags: ["iOS", "Framework", "Xcode"]
categories: ["iOS"]
hero: "images/103735958-841cd100-5032-11eb-86c1-08ab8974be70.png"
menu:
  sidebar:
    name: "앱을 포함한 라이브러리 프로젝트 생성"
    identifier: app-with-framework
    parent: ios
    weight: 5
---

Workspace 를 생성하여 라이브러리와 앱 프로젝트를 생성하는 방식.

1. 우선 빈폴더를 만들고 프로젝트 이름을 정합니다.

   ![newFolder](images/103735958-841cd100-5032-11eb-86c1-08ab8974be70.png)

2. **File > New > Workspace**...을 클릭합니다. Workspace 이름을 지정하고 **Save**.

   ![workspace save](images/103735983-8e3ecf80-5032-11eb-801c-1d589a84092c.png)

3. **File > New > Project...**을 클릭합니다.

   ![newProject](images/103736137-fdb4bf00-5032-11eb-9170-a1e3f849b57c.png)

   

   먼저 앱 프로젝트를 생성하겠습니다.(순서는 상관없음)

   

   ![newapp](images/103736419-90edf480-5033-11eb-8bb6-66d399bc53e7.png)

   

   Product Name 을 정하고 Interface, Life Cycle, Language 각자 선호도에 맞게 선택합니다.

   

   ![create](images/103736439-9b0ff300-5033-11eb-8573-d34a0f73f319.png)

   

   Add to, Group 모두 타겟을 처음 만든 Workspace 를 선택해줍니다.(Framework 생성도 똑같음)

   Framework 도 동일하게 진행하게 되면 프로젝트 폴더구조는 다음과 같습니다.

   

   ![arc](images/103737137-ec6cb200-5034-11eb-8333-dde6581a53e2.png)
