# Fenwick Tree (Binary Indexed Tree)

- Segment Tree와 쓰이는 부분은 똑같고, 공간복잡도와 시간복잡도도 동일하다.
- 그러나 공간이 약간 적게 들고 구현이 더 간단하다.
- Build: O(N) / O(N), Query: O(logN), Update: O(logN)
- N+1 만큼의 공간만 쓴다.
- 그러나 심각한 단점이 있다.
    - Sum이나 곱셈은 구할 수 있지만 max는 구할 수 없다. (역연산이 불가능하기 때문)
    - Tree에 범위를 잘 잡은 prefix sum N+1개를 저장해놓고, 차이를 통해 값을 구하는 방식이기 때문.
- prefix sum을 저장해놓고 사용하는 방식.

## 기본 연산
- update(i, delta): i 위치에 delta를 더하고 상위 노드를 갱신\n
- query(i): 1..i까지의 prefix sum\n
- range sum: query(r) - query(l-1)

```python
def update(i, delta):
    while i <= N:
        tree[i] += delta
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s
```


---
# Fenwick Tree (Binary Indexed Tree, BIT)

## 1. 개념

Fenwick Tree는 **Prefix Sum(누적 합)을 효율적으로 관리하는 자료구조**다.

- Point Update: `O(log N)`
- Prefix Sum Query: `O(log N)`
- Range Sum Query: `O(log N)`
- Space: `O(N)`

일반적으로 **1-based indexing**을 사용한다.

### Segment Tree와 차이

| | Fenwick Tree | Segment Tree |
|---|---|---|
| 구조 | 배열 + 비트 연산 | 이진 트리 |
| 공간 | `N+1` | 보통 `2N~4N` |
| Point Update | `O(log N)` | `O(log N)` |
| Range Sum | `O(log N)` | `O(log N)` |
| Range Min/Max | 일반 BIT로는 어려움 | 가능 |
| Range Update | 별도 기법 필요 | Lazy Propagation |
| 구현 | 간단 | 상대적으로 복잡 |

**추천:** Point Update + Prefix/Range Sum 문제라면 Fenwick Tree가 간결하다.

---

## 2. 핵심: Lowbit

```python
lowbit = i & -i
```

`lowbit(i)`는 정수 `i`의 이진 표현에서 가장 오른쪽에 있는 `1` 비트의 값이다.

**bit[i]가 담당하는 범위:**

```text
[i - lowbit(i) + 1, i]
```

즉, `lowbit(i)`는 해당 노드가 담당하는 원소의 개수다.

### 예시: N = 8

| i | Binary | Lowbit | 담당 구간 |
|---|---|---|---|
| 1 | `0001` | 1 | `[1,1]` |
| 2 | `0010` | 2 | `[1,2]` |
| 3 | `0011` | 1 | `[3,3]` |
| 4 | `0100` | 4 | `[1,4]` |
| 5 | `0101` | 1 | `[5,5]` |
| 6 | `0110` | 2 | `[5,6]` |
| 7 | `0111` | 1 | `[7,7]` |
| 8 | `1000` | 8 | `[1,8]` |

```text
Index:   1  2  3  4  5  6  7  8

bit[1]: [1]
bit[2]: [----]
bit[3]:       [3]
bit[4]: [----------]
bit[5]:             [5]
bit[6]:             [----]
bit[7]:                   [7]
bit[8]: [--------------------]
```

### 예시: i = 12

```text
12       = 00001100
-12      = 11110100
-------------------
12 & -12 = 00000100 = 4
```

따라서 `bit[12]`는 `[9, 12]`의 합을 저장한다.

---

## 3. Query — Prefix Sum

`query(i)`는 **인덱스 1부터 i까지의 합**을 반환한다.

```python
def query(i):
    total = 0

    while i > 0:
        total += bit[i]
        i -= i & -i

    return total
```

### 예시: query(7)

```text
i = 7
  bit[7] → [7,7]
    |
    | i -= lowbit(7) = 1
    v
i = 6
  bit[6] → [5,6]
    |
    | i -= lowbit(6) = 2
    v
i = 4
  bit[4] → [1,4]
    |
    | i -= lowbit(4) = 4
    v
i = 0 (종료)
```

결과:

```text
[1----4] [5--6] [7]
 bit[4]  bit[6] bit[7]
```

```python
query(7) = bit[7] + bit[6] + bit[4]
```

각 구간은 겹치지 않고 `[1,7]` 전체를 덮는다.

**Time: `O(log N)`**

### Range Sum

```python
range_sum(left, right) = query(right) - query(left - 1)
```

---

## 4. Update — Point Update

인덱스 `i`의 값을 `delta`만큼 증가시킨다.

```python
def update(i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i
```

### 예시: update(5, +3)

```text
i = 5 → bit[5] 업데이트
  |
  | + lowbit(5) = 1
  v
i = 6 → bit[6] 업데이트
  |
  | + lowbit(6) = 2
  v
i = 8 → bit[8] 업데이트
  |
  | + lowbit(8) = 8
  v
i = 16 → 종료 (N=8)
```

`bit[5]`, `bit[6]`, `bit[8]` 모두 인덱스 5를 포함하는 구간을 담당하므로 수정해야 한다.

**Time: `O(log N)`**

---

## 5. 전체 Python 구현

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        total = 0

        while i > 0:
            total += self.bit[i]
            i -= i & -i

        return total

    def range_sum(self, left, right):
        return self.query(right) - self.query(left - 1)
```

모든 인덱스는 1-based이며, `update`에는 `1 <= i <= n`을 전달해야 한다.

---

## 6. LeetCode 1649 — Create Sorted Array Through Instructions

### 문제 핵심

숫자 `x`를 삽입할 때:

```text
cost = min(
    x보다 작은 원소 수,
    x보다 큰 원소 수
)
```

실제로 정렬된 배열을 유지할 필요 없이 **각 숫자의 등장 횟수**만 관리하면 된다.

Fenwick Tree를 사용하면:

```python
less = query(x - 1)
greater = inserted_count - query(x)

cost += min(less, greater)

update(x, 1)
```

- `query(x-1)`: x보다 작은 숫자 개수
- `query(x)`: x 이하 숫자 개수
- `inserted_count - query(x)`: x보다 큰 숫자 개수

**중복 값이 있으므로 `greater = total - less`로 계산하면 안 된다.**

전체 복잡도:

- Time: `O(N log M)`
- Space: `O(M)`

`N`: instructions 길이, `M`: 숫자 최댓값

---

## 7. 면접에서 기억할 공식

```python
# 해당 인덱스가 담당하는 구간 크기
lowbit = i & -i

# bit[i] 담당 범위
[i - lowbit + 1, i]

# Prefix Query: 이전 구간으로 이동
i -= lowbit

# Point Update: 현재 원소를 포함하는 다음 구간으로 이동
i += lowbit
```

### 핵심 직관

- **Query:** 작은 인덱스로 이동하면서 서로 겹치지 않는 구간들의 합을 모은다.
- **Update:** 큰 인덱스로 이동하면서 해당 원소를 포함하는 구간들을 수정한다.
- **Segment Tree:** 구간을 절반씩 분할한다.
- **Fenwick Tree:** 인덱스의 마지막 1비트(lowbit)를 이용해 담당 구간을 결정한다.

**한 줄 요약:** Fenwick Tree는 비트 연산을 이용해 Prefix Sum과 Point Update를 모두 `O(log N)`에 처리하는 간결한 자료구조다.
