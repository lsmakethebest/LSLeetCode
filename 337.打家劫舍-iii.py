#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
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
    def rob(self, root: TreeNode) -> int:
        def _rob(node):
            if not node:
                return 0,0 #不偷,偷
            left = _rob(node.left)
            right = _rob(node.right)
            rob_value = node.val + left[0] + right[0]
            not_rob_value = max(left) + max(right)
            return not_rob_value,rob_value
        return max(_rob(root))

        
# @lc code=end

print(max(1,2,3))