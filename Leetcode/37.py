# 스도쿠 문제 풀기! 답은 하나밖에 없다함.

# 걍 겁나 시도하면서 푸는 방법 밖엔 없지 않나?
# 모든 후보를 만든 후에 가장 적은 후보부터 반복해가면서?

# REMIND: backtracking 기본문제.. 근데 못풀었다. 

class Solution:
from typing import List
from collections import defaultdict, deque

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        최적화 : backtracking으로 들어가기전에 가능한 candidate가 가장 적은 emtpy cell을 구하고 거기서 시작.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        triples = defaultdict(set)
        empties = deque()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    rows[i].add(val)
                    cols[j].add(val)
                    triples[(i // 3, j // 3)].add(val)
                else:
                    empties.append((i, j))

        digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

        def dfs() -> bool:
            if not empties:
                return True

            # --- MRV: choose the empty cell with the fewest candidates ---
            best_idx = -1
            best_cands = None

            for idx, (r, c) in enumerate(empties):
                t = (r // 3, c // 3)
                cands = []
                for v in digits:
                    if v not in rows[r] and v not in cols[c] and v not in triples[t]:
                        cands.append(v)

                # If a cell has no candidates, this path is impossible
                if not cands:
                    return False

                if best_cands is None or len(cands) < len(best_cands):
                    best_cands = cands
                    best_idx = idx
                    if len(best_cands) == 1:
                        break

            # Bring best cell to the front of deque
            if best_idx != 0:
                empties.rotate(-best_idx)   # chosen cell moves to front

            r, c = empties[0]
            t = (r // 3, c // 3)

            # Try candidates (already computed by MRV)
            for val in best_cands:
                board[r][c] = val
                rows[r].add(val)
                cols[c].add(val)
                triples[t].add(val)

                empties.popleft()
                if dfs():
                    return True
                empties.appendleft((r, c))

                triples[t].remove(val)
                cols[c].remove(val)
                rows[r].remove(val)
                board[r][c] = "."

            # Restore deque order for upper recursion (undo rotate)
            if best_idx != 0:
                empties.rotate(best_idx)

            return False

        dfs()


    
    def solveSudoku(self, board):
        """
            dict을 사용해서 시간을 좀더 효율적으로,
            원래 이방법으로 풀었는데, 깔끔하게 정리가 안되서 틀린듯.
            이렇게 깔끔하게 푸는 방법을 배우는게 중요하다.
        """
        rows, cols, triples, visit = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visit.append((r, c))
        
        def dfs():
            if not visit:
                return True
            r,c = visit[0]
            t = (r//3, c//3)
            for e in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}: 
                if e not in rows[r] and e not in cols[c] and e not in triples[t]:
                    board[r][c] = e
                    rows[r].add(e)
                    cols[c].add(e)
                    triples[t].add(e)
                    visit.popleft()
                    if dfs():
                        return True
                    board[r][c] = "."
                    rows[r].remove(e)
                    cols[c].remove(e)
                    triples[t].remove(e)
                    visit.appendleft((r, c))
            return False
        dfs()


    def solveSudoku(self, board: List[List[str]]) -> None: # in-place
        """
            정말로 그냥 다해보는 방법..
        """
        def find_unsolved() -> Tuple[int, int]:
            for j in range(9):
                for i in range(9):
                    if board[i][j] == ".":
                        return (i,j)
            return (-1,-1)
    
        def check_available(i, j, e):
            for j_ in range(9):
                if board[i][j_] == e:
                    return False
            for i_ in range(9):
                if board[i_][j] == e:
                    return False
            area_i = i-i%3
            area_j = j-j%3
            for j_ in range(area_j, area_j+3):
                for i_ in range(area_i, area_i+3):
                    if board[i_][j_] == e:
                        return False
            return True
    
        def solve():
            i,j  = find_unsolved()
            if (i,j) == (-1,-1):
                return True
            for e in range(1,10):
                if check_available(i,j,str(e)):
                    board[i][j] = str(e)
                    if solve():
                        return True
                    board[i][j] = "."
            return False
    
        solve()
