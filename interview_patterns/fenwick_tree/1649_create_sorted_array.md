# 1649. Create Sorted Array through Instructions

- [LeetCode 문제](https://leetcode.com/problems/create-sorted-array-through-instructions/)
- **패턴:** Frequency counting + Fenwick Tree (BIT)
- **복잡도:** O(N log V) 시간 / O(V) 공간 (`V=max(instructions)`)
- **중요:** 이전 대화에서 검토한 **DLL + Binary Search**는 일반적으로 O(N log N)이 안 된다. Linked list는 중간 노드로 O(1)에 접근할 수 없고, 이진 탐색을 붙여도 삽입 위치 순위/count를 빠르게 계산하기 어렵다.

## 30초 아이디어

새 값 `x`를 삽입할 때 비용은:

```text
less    = 이전에 들어온 값 중 x보다 작은 원소 수
greater = 이전에 들어온 값 중 x보다 큰 원소 수
cost    = min(less, greater)
```

중복 값은 어느 쪽에도 포함하지 않는다.

Fenwick tree에 **지금까지 등장한 값의 빈도**를 저장하면:

```text
less    = prefix(x-1)
greater = inserted_count - prefix(x)
add(x,1)
```

예: 기존 `[1,2,2,5]`, 새로운 `x=2` → 작은 값 1개, 큰 값 1개 → 비용 1. 동일한 2 두 개는 제외.

## Python

```python
from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        bit = [0] * (max_val + 1)

        def add(i):
            while i <= max_val:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0
        for count, x in enumerate(instructions):
            less = query(x - 1)
            greater = count - query(x)
            ans = (ans + min(less, greater)) % MOD
            add(x)
        return ans
```

## 기억할 포인트

- **정렬 배열을 실제로 만들 필요가 없다**: 필요한 것은 삽입 위치가 아니라 **작은/큰 값 개수**.
- `bisect`로 순위를 찾더라도 Python list 삽입은 O(N) → 전체 O(N²).
- `query(x)`는 `<= x`, `query(x-1)`은 `< x` → 중복 처리 핵심.
- 값이 크거나 음수까지 있다면 coordinate compression 후 index 사용.
