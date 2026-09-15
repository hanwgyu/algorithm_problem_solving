from collections import defaultdict

from functools import lru_cache

class Solution:
   def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        back tracking. 그냥 남은 값이랑 현재 index를 넘겨서 다돔
        """
        candidates.sort()
        print(candidates)
        @lru_cache(None)
        def dfs(index: int, remain: int) -> List[List[int]]:
            if remain == 0:
                return [[]]
            if index >= len(candidates) or candidates[index] > remain:
                return []
            res = list(dfs(index+1, remain))
            for l in dfs(index, remain-candidates[index]):
                res.append([candidates[index]]+l)
            return res
        return dfs(0, target)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        @lru_cache(maxsize=None)
        def dfs(i, target: int) -> List[List[int]]:
            if target == 0:
                return [[]]
            ans = []
            for j in range(i,len(candidates)):
                c = candidates[j]
                if target-c >= 0:
                    for l in dfs(j, target-c):
                        ans.append([c]+l)
            return ans
        return dfs(0, target)


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def findAllCombinations(target: int):
            if target <= 0 or target in visited:
                return
            for c in candidates:
                t = target - c
                if t > 0:
                    findAllCombinations(t)
                    for e in d[t]:
                        if e[-1] <= c:
                            d[target].append(e + [c])
            visited.add(target)

        visited, d = set(), defaultdict(list)
        for c in candidates:
            d[c].append([c])

        findAllCombinations(target)
        return d[target]
