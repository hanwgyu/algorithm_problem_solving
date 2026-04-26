# Solution 1 : 가장 긴 path를 찾아 중간 노드를 리턴. dfs를 돌면서 가장 긴 path 두개를 더해 path를 만들고, 그 중에서 가장 길이가 긴 path를 찾음.
# Time : O(N), Space : O(N)

# Solution 2 : 가장 긴 path를 찾아 중간 노드를 리턴. 임의의 leaf에서 dfs를 돌고, 결과를 이용해 반대편 leaf에서 다시한번 dfs를 돌려 가장 긴 path를 찾음.
# Time : O(N), Space : O(N)

# Solution 3 : inbound 값이 1인 노드들부터 제거하면서 마지막에 남는 노드를 리턴
# Time : O(N), Space :O(N)

from collections import defaultdict
from typing import Set


""" BFS가 더 나음"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        1. 핵심. 아무 노드에서 가장 멀리 있는 노드를 찾으면 그 지점은 반드시 트리의 지름의 한 끝단. 그러고 한번더 가장긴노드 찾은후 가운데 지점 리턴하면 그게 정답.
        그림을 생각해보면 이해가능

        a-e 가 가장긴 길이라 생각하고, 만약 이게 지름이 아니라고 생각한다면, c-d 를 지름으로 가정가능
        1) case 1
        a -x-  n --- c
           |     --- d
           |
           e

        근데 a-e 가 a-x-n-c 나 a-x-n-d 보다 길기때문에 e 는 x-n-c 나 x-n-d보다 길고, 그러면 c 나 d에서 e를 선택하는게 더 길어지는 모순 발생.

        2) case2
        a -n -- c
             -x- d
              |
              e
        a-n-x-e가 제일 긴 길이이면, 이건 a-n-x-d보다 길다. 즉 n-x-e는 n-x-d보다 길기 때문에,  c에서 d로 가는것보다 e로 가는게 더 길어지는 모순 발생.
        """

        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        distances = defaultdict(int)
        def bfs(start: int):
            dist =  defaultdict(int)
            parent = defaultdict(int)

            q = deque([start])
            dist[start] = 0
            farthest = start
            while q:
                node = q.popleft()
                farthest = node
                
                for nei in adj_list[node]:
                    if nei not in dist:
                        dist[nei] = dist[node]+1
                        parent[nei] = node
                        q.append(nei)
            return farthest, parent
        
        a, _ = bfs(0)
        b, parent = bfs(a)

        path = []
        cur = b
        while True:
            path.append(cur)
            if cur == a:
                break 
            cur = parent[cur]
        l = len(path)

        return path[(l-1)//2 : l//2+1]




class Solution:
    def findMinHeightTrees_3(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        """O(N) / O(N)"""
        graph = {v: set() for v in range(n)}
        for f, t in edges:
            graph[f].add(t), graph[t].add(f)
        q, next_q = [v for v in range(n) if len(graph[v]) < 2], []
        while q:
            for v in q:
                for w in graph[v]:
                    graph[w].remove(v)
                    if len(graph[w]) == 1:
                        next_q.append(w)
            ret, q, next_q = q, next_q, []
        return ret

    def findMinHeightTrees_2(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        def build_graph(edges):
            graph = defaultdict(set)
            for i, j in edges:
                graph[i].add(j)
                graph[j].add(i)
            return graph

        def dfs(node, visited):
            visited.add(node)
            rtn = []
            for n in graph[node]:
                if n not in visited:
                    rtn = max([dfs(n, visited), rtn], key=lambda k: len(k))
            rtn.append(node)
            return rtn

        graph = build_graph(edges)
        leaves = [i for i in graph if len(graph[i]) == 1]
        if not leaves:
            return [0]
        print(leaves[0])
        path = dfs(leaves[0], set())
        print(path)
        longest = dfs(path[0], set())
        l = len(longest)
        return longest[(l - 1) // 2 : l // 2 + 1] if longest else [0]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        아무 노드에서나 시작.
        1. 해당 노드와 연결된 노드들 중에 가장 길이가 긴 2개를 찾아 합치면 총 길이가 됨.
        2. 길이가 가장 긴 노드의 중간 지점을 리턴
        """
        if n == 1:
            return [0]
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        
        self.max_l, self.max_node = 0, None 
        def dfs(node: int, visited: Set[int] = set()) -> List[int]:
            """
            leaf까지의 가장 긴 길이의 리스트를 리턴.
            """
            if node in visited:
                return []
            visited.add(node)
            t1, t2 = [], []
            for adj in d[node]:
                t = dfs(adj, visited)
                if len(t) > len(t1):
                    t2, t1 = t1, t
                elif len(t) > len(t2):
                    t2 = t
            if len(t2) + len(t1) + 1 > self.max_l:
                self.max_l = len(t2) + len(t1) + 1
                t = t1+[node]+t2
                self.max_node = t[(self.max_l-1)//2:self.max_l//2+1]
            return t1 + [node]
        dfs(edges[0][0])
        return self.max_node
