#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        cur_level = [root]   
        while cur_level:
            tmp = []
            next_level = []
            for i in cur_level:
                tmp.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            cur_level = next_level
            res.append(tmp)
        return res
        

# @lc code=end

