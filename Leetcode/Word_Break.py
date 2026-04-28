class TrieNode:
    def __init__(self, char: str, end=False):
        self.end = end
        self.char = char
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("", True)

    def insert(self, s: str):
        node = self.root
        for c in s:
            if c not in node.child:
                node.child[c] = TrieNode(c)
            node = node.child[c]
        node.end = True

    def find(self, s: str, start: int, end: int) -> bool:
        node = self.root
        for i in range(start, end):
            c = s[i]
            if c not in node.child:
                return False
            node = node.child[c]
        return node.end

    def findEndsFrom(self, s: str, start: int):
        node = self.root
        for i in range(start, len(s)):
            c = s[i]
            if c not in node.child:
                break
            node = node.child[c]
            if node.end:
                yield i+1

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        trie+dp
        N = len(s)
        M = wordDict 전체 문자 수
        L = wordDict 안의 가장 긴 단어 길이

        Trie : 
            Insert: O(M) / O(M)
            search : O(L) / O(1)

        DP : O(M+NL) / 
        """        

        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        N = len(s)
        dp = [False] * (N+1)
        dp[0] = True

        for i in range(N):
            if not dp[i]:
                continue
            for end in trie.findEndsFrom(s, i):
                dp[end] = True
        return dp[N]




"""
"""


# Solution : DP. 뒷글자부터 시작. 연속으로된 글자를 만들수 있는지 여부를 저장.
# Trie로 단어를 저장해서 관리.
# Time : O(NM), Space : O(N)


class Node:
    def __init__(self, char: str, end=False):
        self.char = char
        self.end = end
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None)

    def addString(self, string: str):
        curr_node = self.root
        for c in string:
            if c not in curr_node.children:
                temp_node = Node(c)
                curr_node.children[c] = temp_node
                curr_node = temp_node
            else:
                curr_node = curr_node.children[c]
        curr_node.end = True

    def findSubstrings(self, string: str):
        ans, curr_node = [], self.root
        for i, c in enumerate(string):
            if c in curr_node.children:
                curr_node = curr_node.children[c]
                if curr_node.end:
                    ans.append(i)
            else:
                return ans
        return ans


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for w in wordDict:
            trie.addString(w)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in reversed(range(len(s))):
            w = s[i:]
            indexs = trie.findSubstrings(w)
            for idx in indexs:
                if i + idx + 1 <= len(s) and dp[i + idx + 1]:
                    dp[i] = True
                    break
        return dp[0]

    
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
