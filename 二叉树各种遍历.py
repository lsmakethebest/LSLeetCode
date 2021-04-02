from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 迭代1
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if color == WHITE:
                # 前序
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))

                # 中序
                # stack.append((WHITE, node.right))
                # stack.append((GRAY, node))
                # stack.append((WHITE, node.left))

                # 后序
                # stack.append((GRAY, node))
                # stack.append((WHITE, node.right))
                # stack.append((WHITE, node.left))

            else:
                res.append(node.val)
        return res


    # 迭代2 是上面迭代的优化(如果存放不是int可能就需要简单修改)
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node,TreeNode):
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
            elif isinstance(node,int):
                res.append(node)
        return res


    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node):
            if node is None:
                return 
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return res


    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node):
            if node is None:
                return 
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node):
            if node is None:
                return 
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res