# Solution 0 : Heuristics. 특정 index의 양옆의 index를 저장하는 list를 둠. 특정 원소 pop되면 해당 list를 수정. Time : O(N!), Space : O(N)

# Solution 1 : 아무것도 없는 상황에서 풍선을 추가해나아감. Recursive.
# Function 'maxCoinsRange(l, r)' : index l+1~r-1까지의 ballon을 추가해나아가는 최대 coin을 리턴.
# Time : O(?), Space : O(N^2) (Worst Case에서 Recursive하게 N, N-1,.... 1의 메모리가 쌓임)
# Leet code Time Limit Exceeded.

# Solution 2 : Solution 1 + DP.
# Time : O(N^3), Space : O(N^2)


class Solution:

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """
        brute force : 터트리는 순서를 바꿔가면서 모두 테스트 N!

        dp 인데 [i...j]에서 k 번째가 가장 마지막에 터트릴때 가장 큰 합이라고 표현함.

        ex) 3 1 5 6
        = "3" + 156 : 3을 가장 마지막 터트릴때
        = 3 + "1" + 56 : 1을 가장 마지막 터트릴때
        = 31 + "5" + 6
        = 315 + "6"
        가장 마지막 남은걸 범위 밖의 i-1, j+1 와 곱해서 최종 sum을 구하면 됨.

        1개짜리, 2개짜리, 3개짜리 점점 늘려감.
        dp[i][j]
        """
        nums = [1] + nums + [1]
        dp = defaultdict(int)
        N = len(nums)
        for i in range(1, N-1):
            dp[(i,i)] = nums[i-1] * nums[i] * nums[i+1]

        for k in range(1, N-2):
            for i in range(1, N-1):
                j = k+i
                if j > N-2:
                    continue 
                dp[(i,j)] = max(dp[(i,l-1)]+ nums[l]*nums[i-1]*nums[j+1] + dp[(l+1, j)] for l in range(i, j+1))
        
        return dp[(1, N-2)]
    
    def maxCoins_2(self, nums: List[int]) -> int:
        def maxCoinsRange(l: int, r: int) -> int:
            if l + 1 == r:
                return 0
            if (l, r) in d:
                return d[(l, r)]
            res = max(
                nums[l] * nums[r] * nums[i]
                + maxCoinsRange(l, i)
                + maxCoinsRange(i, r)
                for i in range(l + 1, r)
            )
            d[(l, r)] = res
            return res

        d = {}
        nums.append(1)
        nums.insert(0, 1)
        return maxCoinsRange(0, len(nums) - 1)

    def maxCoins_1(self, nums: List[int]) -> int:
        def maxCoinsRange(l: int, r: int) -> int:
            if l + 1 == r:
                return 0
            return max(
                nums[l] * nums[r] * nums[i]
                + maxCoinsRange(l, i)
                + maxCoinsRange(i, r)
                for i in range(l + 1, r)
            )

        nums.append(1)
        nums.insert(0, 1)
        return maxCoinsRange(0, len(nums) - 1)
