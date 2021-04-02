#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    # 递归
    # def maxDepth(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     maxLength = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    #     return maxLength

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        height = 0;
        level_size = 1
        while queue:
            node = queue.pop(0)
            level_size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level_size == 0:
                height += 1
                level_size = len(queue)

        return height


# @lc code=end

