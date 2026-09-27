class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """
        n이 작기때문에 사용한 nums를 bit mask로 저장해 memoization.    
        curr_sum을 하나의 bucket을 채우는걸로 생각하고 업데이트.
        이건 직관이 필요없음.
        그리고 큰수부터 넣을 필요도 없다.
        """
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        N = len(nums)

        @lru_cache(None)
        def backtracking(mask, curr_sum):
            if mask == (1<<N)-1:
                return True
            for i in range(N):
                x = nums[i]
                if mask & (1<<i):
                    continue
                if curr_sum+x > target:
                    continue
                if backtracking(mask | (1<<i), (curr_sum+x)%target):
                    return True
            return False
            
        return backtracking(0, 0)

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """
        sum 구해서 k로 나눠.
        그다음 sort해서 채우기 시작하는데, greedy 로 채움? 그게 유일한 해인지 어떻게 암
        그냥 recursive하게 backtracking식으로 돌아야할듯.
        너무 더러운데 유일한 방법인가? 
        """
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)

        buckets = [0] * k
        def backtracking(i: int):
            if i == len(nums):
                return True
            x = nums[i]
            for j in range(k):
                if buckets[j] + x > target:
                    continue
                buckets[j] += x
                if backtracking(i+1):
                    return True
                buckets[j] -= x
                # 직관 : 큰 수부터 계산하기 떄문에 0이면 그냥 패스패버려도 됨. 최적화임.
                if buckets[j] == 0:
                    break
            return False
            
        return backtracking(0)


# Solution : Backtracking + dfs.
# Time : O(k * 2^N), Space : O(N)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def partition(
            nums: List[int],
            visited: List[bool],
            k: int,
            target: int,
            cur: int,
            index: int,
        ) -> bool:
            if k == 1:
                return True
            if cur == target:
                return partition(nums, visited, k - 1, target, 0, 0)
            for i in range(index, len(nums)):
                if not visited[i] and target >= nums[i] + cur:
                    visited[i] = True
                    if partition(
                        nums, visited, k, target, cur + nums[i], i + 1
                    ):
                        return True
                    visited[i] = False
            return False

        if sum(nums) % k != 0:
            return False
        visited = [False] * len(nums)
        return partition(nums, visited, k, sum(nums) // k, 0, 0)
