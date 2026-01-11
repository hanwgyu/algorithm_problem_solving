# Substring Problems

## Sliding Window
- i, j 두 개의 포인터를 두고 j를 기본적으로 움직이면서 조건에 따라 i를 추가로 이동해 답을 구함.
- 둘 다 왼쪽에서 시작한다. 움직이는 윈도우를 이동시키는 개념.
- substring이 특정 조건을 만족하면서 min 또는 max를 구해야할 때, 조건을 만족하면서 포인터를 이동시켜가면서 구해낼 수 있다.
- 숫자가 양수여야 가능하다. r을 움직여서 막히게 되면 l을 움직이고, 이런 식으로 동작해야 하기 때문.
- 예시: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

```python
def minOperations(self, nums: List[int], x: int) -> int:
    """
    Sliding Window

    O(N) / O(1)
    """
    N = len(nums)
    s, l, ans = sum(nums), 1, float('inf')
    nums.insert(0, 0)
    for r in range(N + 1):
        s -= nums[r]
        while l < r and s < x:
            s += nums[l]
            l += 1
        if s == x:
            ans = min(ans, l - 1 + N - r)
    return ans if ans != float('inf') else -1
```

## Prefix Sum
- A[0:]의 값을 저장해나아가서 A[i:j] 범위의 답을 빠르게 계산함.
- 숫자가 양수가 아니어도 가능하다.
- `O(N^2) / O(1)` 문제를 `O(N) / O(N)`으로 줄임.

```python
prefix[0] = 0
prefix[i+1] = prefix[i] + A[i]
# sum(l, r) = prefix[r+1] - prefix[l]
```

## Rolling Hash - Rabin Karp
- 문자열 매칭 알고리즘.
- 각 문자를 정수로 매핑하고, 문자열을 다항식 해시로 표현한다.
- 해시가 같은 경우에만 실제 문자열을 비교해 충돌을 제거한다.
- 길이 m의 윈도우를 한 글자씩 이동하며 해시를 O(1)로 갱신한다.
- 평균 시간: O(n), 최악: O(nm)
- https://github.com/hanwgyu/algorithm_problem_solving/blob/master/Leetcode/1044.py

### Rabin-Karp 핵심 설명
- 길이가 m인 패턴 P를 길이가 n인 문자열 S 안에서 찾는 방법.
- P의 해시값을 먼저 계산하고, S의 모든 길이 m 구간 해시와 비교한다.
- 해시가 같으면 "후보"이므로 실제 문자열을 한 번 더 비교해 충돌을 제거한다.
- 슬라이딩 윈도우로 다음 구간 해시를 O(1)로 갱신한다.

### Rolling Hash 수식
- 문자 값을 정수로 매핑하고, 해시를 다항식으로 만든다.
- H(s[l..r]) = sum(s[i] * BASE^(r-i)) mod MOD
- 다음 구간으로 이동할 때:
  - 이전 해시에서 빠지는 문자 영향을 제거하고
  - 해시에 BASE를 곱한 뒤 새 문자를 더한다.

```python
# remove leading char, shift, add trailing char
# new_hash = (old_hash - s[l] * pow_base[m-1]) * BASE + s[r+1]
```

### 충돌 처리
- 서로 다른 문자열이 같은 해시를 가질 수 있음.
- 실전에서는 1) 해시가 같으면 문자열을 직접 비교하거나, 2) 서로 다른 MOD 두 개를 사용한다.

### 시간 복잡도
- 해시 비교는 O(1), 전체는 O(n)
- 충돌 시 비교를 포함하면 최악은 O(nm)이지만, 일반적으로는 O(n)

## 선택 기준
- Sliding Window 또는 Prefix Sum으로 풀 수 있는지 먼저 고민해보기.
