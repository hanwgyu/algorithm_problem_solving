# Solution : Agent 두개를 동시에 움직인다고 생각하고, 모든 움직임에 대한 dp를 저장.
# Time : O(N^3), Space : O(N^3) (1^2+2^2+3^2+...+N^2)


class Solution:
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        대각선으로 뻗어나감. 그래야 dp가 이전 스텝것이 잘 저장됨.
        i, j, k (스텝수)

        O(N^3) / O(N^2)
        """
        N = len(grid)
        dp = [[float('-inf') for _ in range(N)] for _ in range(N)] # i, j
        dp[0][0] = grid[0][0]
        # k=0인 케이스는 이미 커버됨.
        for k in range(1, 2*N-1):
            # dp 를 초기화해줘야 접근 불가능한 경로가 float('-inf')로 잘 업데이트 됨
            new_dp = [[float('-inf') for _ in range(N)] for _ in range(N)]
            for j in range(N):
                for i in range(N):
                    if k-i < 0 or k-j < 0 or k-i >= N or k-j >=N or grid[i][k-i] == -1 or grid[j][k-j] == -1:
                        continue 
                    gain = grid[i][k-i] + grid[j][k-j] if i != j else grid[i][k-i]
                    new_dp[i][j] = max(
                        dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else float('-inf'), 
                        dp[i][j-1] if j-1 >= 0 else float('-inf'),
                        dp[i-1][j] if i-1 >= 0 else float('-inf'),
                        dp[i][j]
                    ) + gain
            dp = new_dp
        return max(0, dp[N-1][N-1])
        


    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        dfs가 더 풀기 쉬움..
        """
        N = len(grid)

        @lru_cache(None)
        def dfs(x, y, a) -> int:
            b = x+y-a
            if x >= N or y >= N or a >= N or b >= N or grid[x][y] == -1 or grid[a][b] == -1:
                return float('-inf')
            if x == N-1 and y == N-1:
                return grid[N-1][N-1]
            gain = grid[x][y] + grid[a][b]
            if x == a and y == b:
                gain -= grid[x][y]
            return max(dfs(x+1, y, a+1), dfs(x,y+1,a+1), dfs(x+1,y,a),dfs(x,y+1,a)) + gain
        return max(0, dfs(0,0,0))
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        dic = {(0, 0, 0, 0): grid[0][0]}
        N = len(grid)
        for d in range(1, 2 * N - 1):
            locs = (
                [(d - i, i) for i in range(d + 1)]
                if d < N
                else [(d - N + 1 + i, N - 1 - i) for i in range(2 * N - 1 - d)]
            )
            for (x1, y1) in locs:
                for (x2, y2) in locs:
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        dic[(x1, y1, x2, y2)] = -1
                        continue
                    max_cherry = float("-inf")
                    for (x1b, y1b) in [(x1 - 1, y1), (x1, y1 - 1)]:
                        for (x2b, y2b) in [(x2 - 1, y2), (x2, y2 - 1)]:
                            if (
                                0 <= x1b < N
                                and 0 <= y1b < N
                                and 0 <= x2b < N
                                and 0 <= y2b < N
                            ):
                                max_cherry = max(
                                    max_cherry, dic[(x1b, y1b, x2b, y2b)]
                                )
                    if max_cherry == -1:
                        dic[(x1, y1, x2, y2)] = -1
                        continue
                    new_cherry = (
                        grid[x1][y1] + grid[x2][y2]
                        if x1 != x2
                        else grid[x1][y1]
                    )
                    dic[(x1, y1, x2, y2)] = max_cherry + new_cherry
        return (
            dic[(N - 1, N - 1, N - 1, N - 1)]
            if dic[(N - 1, N - 1, N - 1, N - 1)] != -1
            else 0
        )
