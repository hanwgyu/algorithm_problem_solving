# Solution : DP. 각 step에서 마지막 원소까지 1~K개의 인접한 원소중 최대 원소의 총합과 이전 dp를 이용함.
# Time : O(NK), Space: O(N)


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + 1)
        dp[1] = A[0]
        for i in range(1, N):
            dp[i + 1], max_val = dp[i] + A[i], A[i]
            for j in range(1, min(i + 1, K)):
                max_val = max(max_val, A[i - j])
                dp[i + 1] = max(dp[i + 1], dp[i - j] + max_val * (j + 1))
        return dp[N]


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        """
        그냥 dp[k] 만 쓰고 이전 dp 에서 끝내고 새로 시작하는걸로 계산함
        dp[i] = dp[i-1] + 1개
                dp[i-k] + k개 
        O(NK) / O(N) -> O(K)
        
        """
        dp = deque([0]) # 항상 K 개로 유지함.
        for i in range(len(arr)):
            val = arr[i]
            new_val = 0
            new_max = 0
            for length in range(1, min(k, i+1)+1):
                new_max = max(new_max, arr[i+1-length])
                new_val = max(new_val, dp[-length]+ new_max * length)
            dp.append(new_val)
            if len(dp) > k:
                dp.popleft()
        return dp[-1]

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        """
        어쟀든간에 k 길이 안에서 가장 큰걸로 번경해야함.
        dp? - 이때 가장 마지막에서 길이가 몇이였는지도 기록? dp[i][k] 에 합이랑 가장 마지막 k안에 있는 max number?
        dp[i+1][k]구할때에는 
        - dp[i+1][1] 은 심플함. 이전 dp[i][:] 에서 가장 큰값 - 이거 k 번 반복 안하고 dp[i][0]에 업데이트해놓기.
        - dp[i+1][k]는 d[i][k-1]?

        - 마지막에서는 가장 큰값? dp[N][0]?
        O(NK) / O(NK)
        """

        dp = {}
        N = len(arr)
        for k_ in range(k+1):
            dp[(0, k_)] = (arr[0], arr[0])
        for i in range(1, N):
            val = arr[i]

            # k = 1
            dp[(i, 1)] = (dp[(i-1, 0)][0] + val, val)
            dp[(i, 0)] = (dp[(i-1, 0)][0] + val, 0)
            # k > 1
            for k_ in range(2, min(k, i + 1) + 1):
                new_max = max(val, dp[(i-1, k_-1)][1])
                new_sum = dp[(i-1, k_-1)][0] + (new_max - dp[(i-1, k_-1)][1]) * (k_-1)+ new_max
                dp[(i, k_)] = (new_sum,  new_max)
                dp[(i, 0)] = (max(dp[(i, 0)][0], dp[(i, k_)][0]), 0)
        return dp[(N-1, 0)][0]
            


