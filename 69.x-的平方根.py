#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt2(self, x):
        left, right = 0,x//2 + 1
        while left < right:
            mid = (left + right + 1)>>1
            num = mid * mid
            if num > x:
                right = mid -1
            else:
                left = mid
            
        return left
    
    def mySqrt(self,x):
        if x < 2:
            return x
        x0 = x
        x1 = (x0+x/x0)/2
        while True:
            x0 = x1
            x1 = (x0+x/x0)/2
            if (abs(x0-x1) < 1e-6):
                return int(x1)

# @lc code=end

sol = Solution()
print(sol.mySqrt(8))
print(sol.mySqrt2(8))