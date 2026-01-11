# Solution 0 : Brute-force. Time : O(n^2), Space : O(1)

# Solution 1 : DP. 각 위치를 끝으로 하는 palindrome의 모든 start idx를 저장. (is_all_same같이 저장.)
# 1) 매 step마다 현재 위치의 char과 최대 길이 이전의 char이 동일한지 체크.
# 2) 만약 저장된 palindrome의 모든 char이 똑같고, 현재 위치의 char도 똑같으면 이전 위치의 char체크 안하고 추가.
# Time : O(N), Space : O(N)


from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Manaster's Algorithm
        O(N) / O(N)
        """
        R, C = 0, 0
        t = "#" + "#".join(s) + "#"
        N = len(t)
        P = [0] * N
        best_len, best_C = 0,0
        for i in range(N):
            radius = 0
            if i <= R:
                mirror = C - (i-C)
                P[i] = min(P[mirror], R-i)
            while i-(P[i]+1) >= 0 and i+(P[i]+1) < N and t[i+(P[i]+1)] == t[i-(P[i]+1)]:
                P[i] += 1
            if i+P[i] > R:
                R, C = i+P[i], i

            # update best
            if P[i] > best_len:
                best_len = P[i]
                best_center = i
        return s[(best_center - best_len) // 2: (best_center + best_len) // 2] 
    
    def longestPalindrome_1(self, s: str) -> str:
        def updateAns(start, end):
            if len(self.ans) < end - start + 1:
                self.ans = s[start : end + 1]

        if len(s) == 0:
            return ""
        dp, self.ans = [(0, True)], s[0]
        for i in range(1, len(s)):
            temp = []
            for (start_idx, all_same) in dp:
                if start_idx - 1 >= 0 and s[start_idx - 1] == s[i]:
                    if all_same and s[i] != s[i - 1]:
                        all_same = False
                    temp.append((start_idx - 1, all_same))
                    updateAns(start_idx - 1, i)
                elif all_same and s[i] == s[i - 1]:
                    temp.append((start_idx, all_same))
                    updateAns(start_idx, i)
            temp.append((i, True))
            dp = temp
        return self.ans

    def longestPalindrome_0(self, s: str) -> str:
        def findMaxPalindrome(l: int, r: int) -> (int, int):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return (l + 1, r - 1)

        idxes = (0, -1)
        for i in range(len(s)):
            odd_idxes = findMaxPalindrome(i, i)
            even_idxes = findMaxPalindrome(i, i + 1)
            idxes = max(
                [idxes, odd_idxes, even_idxes], key=lambda x: x[1] - x[0]
            )
        return s[idxes[0] : idxes[1] + 1]
