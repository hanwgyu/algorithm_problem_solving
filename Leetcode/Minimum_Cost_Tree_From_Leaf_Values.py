# Solution 1 : DP + dfs. 반씩 잘라가면서 트리의 왼쪽 오른쪽으로 나누고 각 트리의 최소합과 최대 leaf node을 리턴
# Time : O(N^2), Space : O(N^2) (DP없으면 O(N^3)?, O(N))

# Solution 2 : Stack. Leetcode solution 참고함.
# 'Trapping rain water' 문제와 동일하게 감소하는 stack을 유지해나아감. 값이 증가할때는 pop한 값과 min(pop이후 stack 마지막 원소, 추가하려는 원소) 를 곱해서 더함.
# 이게 성립하는 이유는 곱들의 합의 최소값을 구하기 위해서는 곱들이 최대한 작은 값과 많이 계산이 되어야하기 때문.
# 큰 값은 최대한 나중에 곱하고, 작은 값끼리 곱함.
# Time : O(N), Space : O(N)


class Solution:
class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        """
        dp[i][j] : i~j 까지의 array 를 가지고 tree생성했을때 최소의 sum 
        max_val[i][j] : i~j까지의 max
        max 는 O(1)에 구함.
        i...k (left) k+1 ...j(right)
        """
        dp, max_val = defaultdict(int), defaultdict(int)
        N = len(arr)
        for i, n in enumerate(arr):
            max_val[(i,i)] = n

        for l in range(1, N):
            for i in range(N):
                j = i+l
                if j >= N:
                    continue
                dp[(i,j)] = min(dp[(i,k)] + dp[(k+1, j)] + max_val[(i,k)] * max_val[(k+1,j)] for k in range(i, j))
                max_val[(i,j)] = max(max_val[(i,i)], max_val[(i+1, j)])
        return dp[(0, N-1)]

    
    def mctFromLeafValues_2(self, arr: List[int]) -> int:
        st, ans = [float("inf")], 0
        for v in arr:
            while st and st[-1] < v:
                ans += st.pop() * min(st[-1], v)
            st.append(v)
        while len(st) > 2:
            ans += st.pop() * st[-1]
        return ans

    def mctFromLeafValues_1(self, arr: List[int]) -> int:
        def findMinSum(l: int, r: int) -> int:
            if r - l == 1:
                return (0, arr[l])
            if (l, r) in dp:
                return dp[(l, r)]
            ret = float("inf")
            leaf_max = 0
            for i in range(l + 1, r):
                (l_sum, l_max) = findMinSum(l, i)
                (r_sum, r_max) = findMinSum(i, r)
                ret = min(ret, l_sum + r_sum + l_max * r_max)
                leaf_max = max(l_max, r_max)
            dp[(l, r)] = (ret, leaf_max)
            return (ret, leaf_max)

        dp = {}
        return findMinSum(0, len(arr))[0]
