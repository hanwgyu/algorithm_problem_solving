# 222. Count Complete Tree Nodes

- [LeetCode 문제](https://leetcode.com/problems/count-complete-tree-nodes/)
- **핵심:** 완전 이진트리는 마지막 레벨을 제외하고 꽉 차 있다.
- **복잡도:** O(log² N) 시간 / O(log N) 재귀 스택 (아래 코드). 일반 트리 노드 세기는 O(N).

## 30초 아이디어

현재 서브트리의 **가장 왼쪽 경로 높이**와 **가장 오른쪽 경로 높이**가 같다면 완전 이진트리의 성질상 그 서브트리는 **perfect binary tree**.
그래서 노드를 하나씩 탐색할 필요 없이 `2^height - 1`로 바로 계산한다.

```text
      1              h(left)=3, h(right)=3
     /              => 2^3-1 = 7 nodes
    2   3
   /\   /\
  4  5 6  7
```

높이가 다르면 `1 + count(left) + count(right)` 재귀 호출.

## Python

```python
from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0
        lh = left_height(root)
        rh = right_height(root)
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

## 주의

- **완전(complete)**과 **포화(perfect)**는 다름. 높이가 같으면 해당 서브트리가 perfect인 것은 **complete 트리라는 전제** 때문에 성립.
- 높이는 **노드 수 기준** (빈 트리 0).
- 왼쪽/오른쪽 극단 경로만 확인한다.
- 면접에서 O(log² N)의 이유: 재귀 깊이 O(log N), 각 단계 높이 측정 O(log N).
