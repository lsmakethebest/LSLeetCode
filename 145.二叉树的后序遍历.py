#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node,TreeNode):
                stack.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            elif isinstance(node,int):
                res.append(node)
        return res

# @lc code=end

