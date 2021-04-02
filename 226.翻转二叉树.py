#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    # 递归 前中后序遍历均可实现
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root is None:
    #         return root
        
    #     root.left,root.right = root.right,root.left
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)
    #     return root

    # 非递归 
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left,node.right = node.right,node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

# @lc code=end

