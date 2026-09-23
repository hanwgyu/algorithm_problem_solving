# Solution 1 : inorder traverse해서 이상한 두 노드를 찾고 두 노드의 값을 바꿈.
# val값이 작아질 때가 두번 발생하면 첫번째는 앞쪽노드, 두번째는 뒤쪽노드가 바뀐노드.
# Time : O(N), Space : O(H)

# Solution 2 : Morris Preorder Traversal. Space를 사용하지 않는 preorder traversal. 맨 오른쪽 자식 노드를 부모노드에 연결해 stack없이 iterate이후 위로 올라오게 동작시킴.
# node가 오른쪽 자식으로 이동할때 (올라오거나, 오른쪽으로 내려갈때)만 pre_n과의 크기를 비교함.
# Time : O(N), Space : O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.

        Morris inorder-traversal

        parent로 올라올떄 next를 parent로 연결해놔서 올라옴

        1. curr.left -> find rightmost node and connect curr to the node's right
        2. go left, do the same
        3. when back to curr, check the same 1 - if there is node on the right, then disconnect the node and go down right
        """

        curr = root

        first, second = None, None
        prev = None
        def visit(node):
            nonlocal first, second, prev
            # Find two nodes
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr
            prev = curr

        while curr:
            if not curr.left:
                visit(curr) #Important!!!
                curr = curr.right
            else:
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    visit(curr) #Important!!!
                    curr = curr.right
        first.val, second.val = second.val, first.val


class Solution:
    """
    Do not return anything, modify root in-place instead.
    """

    def recoverTree_2(self, root: TreeNode) -> None:
        n1 = n2 = pre_n = None
        node = root
        while node:
            if node.left:
                temp = node.left
                while temp.right and temp.right != node:
                    temp = temp.right
                if not temp.right:
                    # 노드를 연결
                    temp.right = node
                    node = node.left
                else:
                    # parent로 올라온 후.
                    # 로직
                    if pre_n and pre_n.val > node.val:
                        n2 = node
                        if not n1:
                            n1 = pre_
                    pre_n = node
                    # 노드가 연결되어 있으므로 끊고 오른쪽으로 내려간다.
                    temp.right, node = None, node.right
            else:
                if pre_n and pre_n.val > node.val:
                    n2 = node
                    if not n1:
                        n1 = pre_n
                pre_n = node
                node = node.right
        n1.val, n2.val = n2.val, n1.val

    def recoverTree_1(self, root: TreeNode) -> None:
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            if self.pre_n and self.pre_n.val > node.val:
                self.n2 = node
                if not self.n1:
                    self.n1 = self.pre_n
                else:
                    return
            self.pre_n = node
            inorder(node.right)

        self.n1 = self.n2 = self.pre_n = None
        inorder(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
