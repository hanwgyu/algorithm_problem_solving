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

## 선택 기준
- Sliding Window 또는 Prefix Sum으로 풀 수 있는지 먼저 고민해보기.
