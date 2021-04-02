#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        y = abs(x)
        boudary = (1<<31) - 1 if x>0 else 1<<31 
        while y != 0:
            count = count*10+y%10
            y=y//10
            if count > boudary:
                return 0
        return count if x>0 else -count

# @lc code=end

# 复杂度分析:
# 时间复杂度：O(log(x)), x中大约有y个数字，其中10^y = x ==> y = log(x)
# 空间复杂度：O(1)
