---
title: 배시 변수
weight: 210
menu:
  notes:
    name: 변수
    identifier: notes-bash-variables
    parent: notes-bash
    weight: 10
---

<!-- 변수 -->
{{< note title="변수" >}}

```bash
NAME="John"
echo $NAME
echo "$NAME"
echo "${NAME}
```

{{< /note >}}

<!-- 조건문 -->
{{< note title="조건문" >}}

```bash
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi
```

{{< /note >}}