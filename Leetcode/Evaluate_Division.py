# Solution1 : 값을 표시하는 Vertex to Vertex list를 만들고, 모든 노드에서 모든 노드까지 경로값을 업데이트. 중간 노드에 대해 iteration. Floyd-Warshall과 동일한 방식.
# hash의 hash를 사용하여 경로값을 표시.
# Time : O(V^3), Space : O(V^2)

from collections import defaultdict


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        """
        Floyd-Warshall

        기본적으로 DP. 
        dist[k][i][j] = 중간 노드로 {0..k}만 허용했을 때 i에서 j까지의 최단거리
        
        dist[k][i][j] = min(dist[k-1][i][j], dist[k-1][i][k] + dist[k-1][k][j])
        
        로 할 수 있는데 inplace로 해서 아래와 같이 줄임.

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )
        """
        vals = defaultdict(lambda: defaultdict(lambda: -1.0))
        for (src, dst), val in zip(equations, values):
            vals[src][src] = vals[dst][dst] = 1.0
            vals[src][dst] = val
            vals[dst][src] = 1.0 / val

        for mid in vals.keys():
            for src in vals[mid]:
                for dst in vals[mid]:
                    vals[src][dst] = vals[src][mid] * vals[mid][dst]

        return [vals[query[0]][query[1]] for query in queries]

    def calcEquation_2(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        vals = defaultdict(lambda: defaultdict(lambda: -1.0))
        inputs = defaultdict()
        for i in range(len(equations)):
            src, dst, val = equations[i][0], equations[i][1], values[i]
            vals[src][dst] = val
            vals[dst][src] = 1.0 / val
            inputs[src] = True
            inputs[dst] = True

        for src in inputs.keys():
            for dst in inputs.keys():
                if src == dst:
                    vals[src][dst] = 1.0
                    continue
                elif src in vals and dst in vals[src]:
                    continue
                for mid in inputs.keys():
                    if (
                        src in vals
                        and mid in vals[src]
                        and mid in vals
                        and dst in vals[mid]
                    ):
                        res = vals[src][mid] * vals[mid][dst]
                        vals[src][dst] = res
                        break

        return [vals[query[0]][query[1]] for query in queries]
