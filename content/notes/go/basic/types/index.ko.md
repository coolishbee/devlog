---
title: 기본 자료형
weight: 20
menu:
  notes:
    name: 기본 자료형
    identifier: notes-go-basics-types
    parent: notes-go-basics
    weight: 20
---
<!-- 문자열 자료형 -->
{{< note title="문자열" >}}
```go
str := "Hello"
```

여러 줄 문자열
```go
str := `Multiline
string`
```
{{< /note >}}

<!-- 숫자 자료형 -->
{{< note title="숫자" >}}
자주 사용하는 자료형

```go
num := 3          // int
num := 3.         // float64
num := 3 + 4i     // complex128
num := byte('a')  // byte (alias for uint8)
```

그 밖의 자료형

```go
var u uint = 7        // uint (unsigned)
var p float32 = 22.7  // 32-bit float
```

{{< /note >}}

<!----------- 배열  ------>

{{< note title="배열" >}}

```go
// var numbers [5]int
numbers := [...]int{0, 0, 0, 0, 0}
```

{{< /note >}}

<!-- 포인터 -->

{{< note size="medium" title="포인터">}}

```go
func main () {
  b := *getPointer()
  fmt.Println("Value is", b)
```

```go
func getPointer () (myPointer *int) {
  a := 234
  return &a
```

```go
a := new(int)
*a = 234
```

포인터는 변수가 저장된 메모리 위치를 가리킵니다. 고 언어는 사용하지 않는 메모리를 자동으로 회수합니다.

{{< /note >}}

<!-- 자료형 변환 -->

{{< note title="자료형 변환" >}}

```go
i := 2
f := float64(i)
u := uint(i)
```

{{< /note >}}

<!-- 슬라이스 -->

{{< note title="슬라이스" >}}

```go
slice := []int{2, 3, 4}
```

```go
slice := []byte("Hello")
```

{{< /note >}}
