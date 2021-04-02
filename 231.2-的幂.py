#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo2(self, n: int) -> bool:
            x = 2
            if n == 0:
                return 1
            result = self.isPowerOfTwo(n//2)
            result *= result
            return result if n & 1 == 0 else result * x

    def isPowerOfTwo(self, n: int) -> bool:
            x = 2
            result = 1
            while n != 0:
                if n & 1 == 1:
                    result *= x
                x *= x
                n >>= 1
            return result




# @lc code=end

print(Solution().isPowerOfTwo(10))
print(Solution().isPowerOfTwo2(10))