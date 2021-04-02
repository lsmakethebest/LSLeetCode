#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        count = len(nums)
        for i in range(count):
            if (target - nums[i]) in dic:
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]] = i
            
# @lc code=end

