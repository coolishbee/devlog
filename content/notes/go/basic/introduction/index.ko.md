---
title: 소개
weight: 10
menu:
  notes:
    name: 소개
    identifier: notes-go-basics-intro
    parent: notes-go-basics
    weight: 10
---
<!-- 프로그램 예제 -->
{{< note title="첫 프로그램">}}
고 언어로 작성한 간단한 프로그램입니다.

```go
package main

import "fmt"

func main() {
  message := greetMe("world")
  fmt.Println(message)
}

func greetMe(name string) string {
  return "Hello, " + name + "!"
}
```

다음 명령으로 프로그램을 실행합니다.

```bash
$ go run hello.go
```
{{< /note >}}

<!-- 변수 선언 -->

{{< note title="변수" >}}
**일반적인 선언:**
```go
var msg string
msg = "Hello"
```

---

**짧은 선언:**
```go
msg := "Hello"
```
{{< /note >}}


<!-- 상수 선언 -->

{{< note title="상수" >}}
```go
const Phi = 1.618
```
{{< /note >}}
