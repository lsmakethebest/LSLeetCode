#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:

    def myPow(self, x: float, n: int) -> float:
            if n == 0:
                return 1.0
            if n == -1:
                return 1 / x
            result = self.myPow(x,n//2)
            result *= result
            return result if n & 1 == 0 else result * x


    def myPow2(self, x: float, n: int) -> float:
            y = abs(n) 
            result = 1.0
            while y != 0:
                if y & 1 == 1:
                    result *= x
                x *= x
                y >>= 1
            return result if n > 0 else 1 /result 




# @lc code=end

print(Solution().myPow(2.0,-4))
print(Solution().myPow2(2.0,-4))

