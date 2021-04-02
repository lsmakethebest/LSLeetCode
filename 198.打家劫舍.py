#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]

        first = nums[0]
        second = max(nums[0],nums[1])

        for i in range(2,size):
            first,second =second,max(first+nums[i],second)
        return second


    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[size-1]



# @lc code=endπ

