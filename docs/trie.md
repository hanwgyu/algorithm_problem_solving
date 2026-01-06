# Trie

```python
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            # children에 TrieNode가 없으면, 새로운 TrieNode를 생성함
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    # iterate하면서 결과 찾기
    def find_sentences(self, s: str, node: TrieNode) -> list[tuple[str, int]]:
        """
        s: 현재 노드까지의 str
        """
        if not node:
            return []
        ans = []
        if node.times != 0:
            ans.append((s, node.times))
        for child in node.child.values():
            ans.extend(self.find_sentences(s + child.c, child))
        return ans
```
