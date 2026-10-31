# Fenwick Tree (Binary Indexed Tree) — 1분 복습

**용도:** 값 하나를 변경하면서 prefix sum을 빠르게 구하기. update와 prefix sum 모두 **O(log N)**, 공간 **O(N)**.

## 핵심 비트 연산

`lowbit(i) = i & -i` = 이진수에서 맨 오른쪽 1비트.

```text
index: 1  2  3  4  5  6  7  8
lowbit:1  2  1  4  1  2  1  8

tree[6]는 원본 인덱스 5..6의 합
tree[8]은 원본 인덱스 1..8의 합
```

- **update(i,delta):** `i += i & -i` (관련 상위 구간으로 올라감).
- **query(i):** `i -= i & -i` (prefix를 이루는 구간을 하나씩 떼어냄).
- 편하게 쓰려면 **1-indexed**.

```python
class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def prefix(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total

    def range_sum(self, l, r):
        return self.prefix(r) - self.prefix(l - 1)
```

**실수:** `add(0,...)`은 무한루프. 값의 범위가 크면 **coordinate compression** 먼저.

활용 문제: [1649 Create Sorted Array through Instructions](1649_create_sorted_array.md)
