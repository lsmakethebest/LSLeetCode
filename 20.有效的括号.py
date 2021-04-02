#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {']':'[','}':'{',')':'('}
        stack = []
        for sub in s:
            if sub in dic:
                # 是右括号
                if len(stack) == 0 or stack.pop() != dic[sub]:
                    return False
            else:
                stack.append(sub)
        return len(stack) == 0

# @lc code=end

sol = Solution()
print(sol.isValid('[[[]]]'))