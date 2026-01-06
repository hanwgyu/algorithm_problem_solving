# Graph

## Union-Find
- Union by Rank 최적화: depth가 짧은 쪽을 긴 쪽에 연결.
- Path Compression 최적화: find 시 depth를 1로 줄임.
- 예시: https://github.com/hanwgyu/algorithm_problem_solving/blob/master/Leetcode/547.py

```python
from collections import defaultdict

d = defaultdict(int)  # key: city id(0 ~ N-1), value: province id (0~ N-1)
N = len(A)
for i in range(N):
    d[i] = i
L = [0] * N  # Union by rank 최적화를 위한 길이 저장

def union(c1: int, c2: int):
    p1, p2 = find(c1), find(c2)
    if p1 != p2:
        """
        Union by rank 최적화 : https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3879/
        """
        if L[p1] > L[p2]:
            d[p2] = p1
        elif L[p1] == L[p2]:
            # 사실상 길이가 같을때만 업데이트 된다. 한쪽이 더 길때는 긴 길이가 유지되기 때문.
            L[p2] += 1
            d[p1] = p2
        else:
            d[p1] = p2

def find(c: int) -> int:
    """
    O(N) -> O(logN) (Union by rank) -> O(1) (Path compression)
    """
    if c == d[c]:
        return c
    """
    Path Compression. 단 한줄이면 된다. https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/
    """
    d[c] = find(d[c])
    return d[c]
```

## Topological Sort
- indegree가 1인 노드를 queue에 넣고 순차적으로 방문.

## Minimum Spanning Tree
- https://leetcode.com/problems/min-cost-to-connect-all-points/
- Prim's Algorithm
    - 하나의 그룹을 크게 만들어가면서 구름을 퍼트리듯이.
    - 임의의 노드에서 시작해 노드들과 연결된 vertex들 중 가장 짧은 것을 추가한다.
    - visited 정보를 관리해서, 노드를 두 번 방문하지 않기 때문에 사이클이 생기지 않게 한다.
    - 연결된 가장 짧은 vertex를 찾기 위해 heap 사용.
- Kruskal's Algorithm
    - 역병 퍼지듯이 그룹을 만듬.
    - 짧은 순서대로 edge를 찾고, cycle을 만들지 않으면 추가한다.
    - Union-Find를 사용해 cycle이 생기는지를 판단한다.
- 비교
    - Kruskal's 알고리즘
        - O(ElogE + ElogV) / O(V^2)
            - 에지 정렬 시: O(ElogE)
            - Union Find: O(logV)
        - 에지가 많지 않은 희소 그래프(sparse graph)에서 효과적.
    - Prim 알고리즘
        - heap 사용 시: O((E + V)logE) / O(E)
        - Fibonacci Heaps을 사용 시 최적의 성능
            - 키 감소(decrease key)와 최소값 삭제(delete min) 연산에서 뛰어난 성능.
            - 키 감소: O(1)의 상한.
            - 최소값 삭제: O(logN)의 상한.
            - 에지가 많은 밀집 그래프(dense graph)나, 에지의 추가/삭제가 빈번한 경우에 더 적합.
    - The best time for Kruskal's is O(E logV). For Prim's using fib heaps we can get O(E + V logV). Therefore on a dense graph, Prim's is much better.

## Shortest Path

### Dijkstra's Algorithm
- 하나의 정점에서 다른 모든 정점까지의 최단 경로 구함.
- 시작 노드에서 주변 노드까지의 거리를 업데이트.
    - 초기화: 시작 노드의 거리를 0으로 설정하고, 다른 모든 노드의 거리는 무한대로 설정.
- 방문하지 않은 노드 집합: 아직 방문하지 않은, 최단 거리의 노드를 방문 리스트에 추가하며, 그 노드부터 주변 노드의 거리를 이용해 시작 노드에서 주변 노드까지의 거리를 업데이트.
- heap 사용.
- 말이 되는 이유? 증명
    - 업데이트하는 과정에서 시작 노드 S에서 가장 짧은 거리인 노드 A를 방문한다고 가정하면, 방문된 시점에 항상 가장 짧은 길이가 보장된다.
    - 이후, 더 먼 노드 B에서 추가로 이동해서 A로 오게 되면, (S->B + B->A) 길이가 되고, S->B가 이전 S->A보다 이미 긴 상태여서 절대로 다시 업데이트 되지 않는다.
- 업데이트를 진행할 때 이전 노드를 저장해서 경로를 구할 수 있다.
- O((V+E)logE) = O((V+E)logV), Space: O(V+E)
- https://leetcode.com/problems/network-delay-time/

```python
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    cost = defaultdict(lambda: float('inf'))
    cost[k] = 0
    adj_list = defaultdict(list)
    h = [(0, k)]  # time, src
    visited = set()
    # make adjacent list
    for src, dst, time in times:
        adj_list[src].append((dst, time))
    # start from node k
    while h and len(visited) < n:
        src_time, src = heapq.heappop(h)
        if src in visited:
            continue
        visited.add(src)
        for dst, time in adj_list[src]:
            if cost[dst] > src_time + time:
                cost[dst] = src_time + time
                heapq.heappush(h, (src_time + time, dst))
    print(cost)
```

### Floyd-Warshall
- 모든 정점에서 다른 모든 정점까지의 최단 경로 구함.
- 기존에 주어진 모든 경로의 cost를 저장.
- 모든 경로 i->j 까지를 확인하면서, 중간에 k를 거쳐갈 때의 cost와 비교해서 업데이트 진행.
- 일부 edge의 값이 없을 때는 알고리즘을 시작할 때 해당 edge를 무한대로 설정하면 된다.

```python
for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[(i, j)] = min(cost[(i, j)], cost[(i, k)] + cost[(k, j)])
```

## Eulerian Trail
1. 차수 확인: 모든 노드의 차수를 확인하여 0개 또는 2개의 홀수 차수 노드가 있는지 확인.
2. 경로 찾기
    - 홀수 차수 노드가 없다면, 그래프의 어느 노드에서나 시작할 수 있다.
    - 홀수 차수 노드가 있다면, 그 중 하나에서 시작한다.
3. DFS 알고리즘으로 구성.

```python
# graph: adjacency list
def dfs(node):
    while graph[node]:
        next_node = graph[node].pop()
        dfs(next_node)
    path.append(node)

path = []
dfs(start)
return path[::-1]  # 역순으로 반환
```

- 예시: https://leetcode.com/problems/reconstruct-itinerary/description/

## Others
- 그래프가 loop가 없는지 확인.
- Tree Centering: 특정 노드를 루트로 하여 트리의 깊이를 최소화하는 알고리즘.
    - https://leetcode.com/problems/binary-tree-maximum-path-sum/
    - https://leetcode.com/problems/minimum-height-trees/submissions/735039485/

## Bellman-Ford
- TODO: 정리 필요
