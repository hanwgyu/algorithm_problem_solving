# Backtracking

## 템플릿

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

## Notes
- 예시: https://leetcode.com/problems/sudoku-solver/
- 범위 예외처리를 어떻게 해야 하는지 유의할 것.
    - 예시: https://github.com/hanwgyu/algorithm_problem_solving/blob/master/Leetcode/Word_Search.py
- deepcopy를 잘 생각하기.

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(cur: List[int], visited: Set[int]):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for num in nums:
                if num not in visited:
                    cur.append(num)
                    visited.add(num)
                    dfs(cur, visited)
                    visited.remove(num)
                    cur.pop()

        dfs([], set())
        return ans
```
