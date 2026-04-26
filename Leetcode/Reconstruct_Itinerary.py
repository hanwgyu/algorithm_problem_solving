# Solution : 한붓그리기. DFS를 통해 만약 더이상 갈곳이 없으면 값을 저장.

# adjacent list를 만들고, dfs로 알파벳 순으로 방문하고, 방문할 노드가 없으면 추가한 후, 거꾸로 뒤집으면 답이 나온다.

# Time : O(E), Space : O(E+V)

from collections import defaultdict


class Solution:

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        """
        한붓그리기 

        brute-force : O(N!) / O(1)

        in, out 의 차이가 최대 1까지만 나야함.
        in - out = 1 : 끝나는 곳.
        in - out = -1 : 시작
        in - out = 0 : 중간 노드.

중간 노드는 항상 들어가는 edge와 나가는 edge가 같기 때문에 여기서 멈춘다는게 말이 안됨. 이미 들어온 상태이기 때문에 나갈수 있어야한다.

결론적으로 막힐 수 있는 노드는:

끝점 (in - out = +1): 원래 들어오는 게 1개 더 많으니까 당연히 막힘
시작점 (out - in = +1): 모든 간선 소진 후 최종적으로 여기서 막힘

따라서 dfs. 로 마음대로 돌면서 막힌 부분부터 넣고 뒤집으면 정상 경로가 나옴.
        """
        d, ans = defaultdict(list), []
        for src, dst in sorted(tickets, reverse=True):
            d[src].append(dst)

        def dfs(src: str):
            while d[src]:
                dst = d[src].pop()
                dfs(dst)
            ans.append(src)
        dfs("JFK")
        return ans[::-1]
