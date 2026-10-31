# 내 풀이 — Row Histogram + DP + Monotonic Stack

- 문제: [LeetCode 1504. Count Submatrices With All Ones](https://leetcode.com/problems/count-submatrices-with-all-ones/)
- 시간 **O(MN)** / 추가 공간 **O(N)**

**30초 복습:** 각 행을 아래쪽 끝으로 고정하고 열마다 연속된 1의 높이 `heights[j]`를 갱신한다. `dp[j]`는 현재 `j`를 **오른쪽 끝**으로 하는 모든 사각형 수. 증가 스택에서 이전의 `height <= h`인 가장 가까운 열 `prev_idx`를 찾아 두 그룹으로 나눈다.

- 시작 열이 `prev_idx`보다 **오른쪽**이면 현재 높이 `h`가 최소 → `(j-prev_idx)*h`.
- 시작 열이 `prev_idx` **이전 또는 동일**이면 → `dp[prev_idx]` 재사용.
- 두 그룹은 시작 위치가 겹치지 않음. 각 행/열을 하단/우측 끝으로 고정하므로 최종 합계도 중복 없음.

```text
heights = [2,4,3], j=2, prev_idx=0
start 1,2: 3 + 3 = 6
start 0:   dp[0] = 2
dp[2] = 8
```

### 내 코드 (sentinel 경계조건 수정)

원래 생각과 구성은 그대로 유지하고 **두 부분만 수정**:
1. `st=[(-1,0)]` sentinel은 절대로 pop하면 안 되므로 `len(st)>1`.
2. `prev_idx=-1`일 때 `dp[-1]`을 조회하면 Python의 **마지막 원소**가 되어 오류가 날 수 있음 → `0` 처리.

```python
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        """
        각 행을 histogram의 바닥으로 보고 각 열의 연속된 1 높이를 갱신.
        dp[j] = 현재 행과 열 j를 끝으로 하는 사각형 수.
        이전 작은/같은 높이의 위치를 increasing stack에서 찾는다.

        cnt = (j - prev_idx) * h + dp[prev_idx]
        prev_idx == -1이면 이전 dp는 0.

        O(MN) time / O(N) space
        """
        M, N = len(mat), len(mat[0])
        res = 0
        heights = [0] * N

        for i in range(M):
            dp = [0] * N
            st = [(-1, 0)]  # (index, height); sentinel
            for j in range(N):
                h = 0 if mat[i][j] == 0 else heights[j] + 1
                heights[j] = h

                while len(st) > 1 and st[-1][1] > h:
                    st.pop()

                prev_idx, _ = st[-1]
                prev_cnt = dp[prev_idx] if prev_idx != -1 else 0
                cnt = (j - prev_idx) * h + prev_cnt

                dp[j] = cnt
                res += cnt
                st.append((j, h))

        return res
```

**자주 틀리는 점:** 전체 `a*b`의 사각형 수 공식은 이 풀이에 필요하지 않음. **현재 오른쪽 끝의 구간별 minimum 높이 합**만 구하면 됨. Stack에 동일 높이는 남겨도 올바르게 계산됨 (`while > h`).

---

# 1504. Count Submatrices With All Ones

- [LeetCode 문제](https://leetcode.com/problems/count-submatrices-with-all-ones/)
- **패턴:** Histogram + Monotonic Stack (+ DP)
- **복잡도:** O(MN) 시간 / O(N) 공간

## 30초 핵심

각 행을 **사각형의 아래쪽 끝**으로 고정. `height[j]` = 그 행에서 위로 연속된 1의 수.
해당 행에서 각 **오른쪽 끝 j**를 고정하고, 가능한 모든 **왼쪽 시작점**에 대해 최소 높이를 더한다.

```text
height = [2,4,3]  (오른쪽 끝 = 2)

왼쪽 시작점 2: [3]     최소 3 -> 3개
왼쪽 시작점 1: [4,3]   최소 3 -> 3개
왼쪽 시작점 0: [2,4,3] 최소 2 -> 2개
총 8개
```

**왜 중복이 없는가?** 매 사각형은 (아래쪽 행, 오른쪽 열, 왼쪽 열, 높이)로 유일하게 결정된다. `count`는 **현재 오른쪽 끝**인 사각형만 계산한다.

## 방법 A: 이전 count를 높이 차이만큼 수정 (추천 직관)

- `count`는 현재 열에서 끝나는 사각형 개수.
- `stack = [(height, width)]`: 동일한 최소 높이로 묶인 **왼쪽 시작점 수** (`width`).
- 새 열 `h`에서 시작하는 구간 하나 추가 → `count += h`.
- 이전 시작점 그룹의 높이가 `h`보다 높다면, 높이가 감소한 만큼 `(old_h-h)*width`를 **빼고**, 해당 시작점들을 새 그룹에 합친다.

```text
height [2,4] -> count=2+4=6
height 3 추가:
    새로운 시작점 +3
    기존 높이 4 -> 3: -1
    기존 높이 2 -> 2: 그대로
=> 6+3-1 = 8
stack [(2,1),(3,2)]
```

```python
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        height = [0] * n
        ans = 0
        for row in mat:
            stack = []  # (minimum height, number of start positions)
            count = 0   # rectangles ending at current column
            for j, x in enumerate(row):
                height[j] = height[j] + 1 if x else 0
                h = height[j]
                count += h               # new start at j
                width = 1
                while stack and stack[-1][0] >= h:
                    old_h, old_width = stack.pop()
                    count -= (old_h - h) * old_width
                    width += old_width
                stack.append((h, width))
                ans += count
        return ans
```

## 방법 B: 이전 작은 높이의 DP 재사용

`dp[j]` = 현재 열 `j`에서 끝나는 사각형 수.
`k` = `height[j]`보다 **엄격하게 작은** 가장 가까운 왼쪽 index (없으면 -1).

- 시작점 `k+1...j`: 최소 높이 `height[j]`, 따라서 `(j-k)*height[j]`.
- 시작점 `0...k`: 최소 높이가 이미 `k`까지의 구간에서 결정되므로 `dp[k]` 재사용.
- 겹치지 않는 시작점 그룹 둘을 합침.

```text
[2,4,3], j=2, k=0
start 1,2 => 3*2=6
start 0   => dp[0]=2
dp[2]=8
```

```python
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        height = [0] * n
        ans = 0
        for row in mat:
            dp = [0] * n
            stack = []  # indices with strictly increasing height
            for j, x in enumerate(row):
                height[j] = height[j] + 1 if x else 0
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()
                if stack:
                    k = stack[-1]
                    dp[j] = dp[k] + (j-k)*height[j]
                else:
                    dp[j] = (j+1)*height[j]
                ans += dp[j]
                stack.append(j)
        return ans
```

## 실수 포인트

- Stack은 rectangle들을 직접 세는 도구가 아니라, **같은 최소 높이 그룹(A)** 또는 **가장 가까운 작은 높이(B)**를 찾는다.
- 방법 A의 `count`는 누적 답 `ans`가 아니다. **한 행의 현재 오른쪽 끝**에 대한 개수다.
- `height[j]=0`에서도 A/B 정상 작동.
- 기존에 작성한 `st=[(-1,0)]` 방식은 **sentinel을 pop하지 않도록** `while len(st)>1 ...`을 써야 한다. `h[-1]`을 실제 높이로 해석하면 오류가 난다.
- 기존 코드처럼 열을 바깥 루프로 돌리고 연속된 1을 가로 방향으로 쌓아도 동등하다.

**다음 복습 질문:** [2,4,3]에서 왜 8개인가? 방법 A의 `width`는 무엇을 세는가?
