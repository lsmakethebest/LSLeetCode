#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
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

        def my_rob(new_nums: List[int]) -> int:
            if not new_nums:
                return 0
            size = len(new_nums)
            if size == 1:
                return new_nums[0]

            first = new_nums[0]
            second = max(new_nums[0],new_nums[1])

            for i in range(2,size):
                first,second =second,max(first+new_nums[i],second)
            return second

        return max(my_rob(nums[:-1]),my_rob(nums[1:]))

# @lc code=end

Solution().rob([2,3,3])