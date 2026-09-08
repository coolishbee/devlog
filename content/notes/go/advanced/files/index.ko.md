---
title: 파일 다루기
weight: 40
menu:
  notes:
    name: 파일 다루기
    identifier: notes-go-advanced-files
    parent: notes-go-advanced
    weight: 10
---

<!-- 조건문 -->
{{< note title="조건문">}}

```go
if day == "sunday" || day == "saturday" {
  rest()
} else if day == "monday" && isTired() {
  groan()
} else {
  work()
}
```

```go
if _, err := doThing(); err != nil {
  fmt.Println("Uh oh")
```

{{< /note >}}