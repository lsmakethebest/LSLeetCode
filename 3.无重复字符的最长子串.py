#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        if s is None:
            return 0
        count = len(s)
        if count <= 0:
            return 0
        longest = 1
        start = 0
        dic = {}
        for i, c in enumerate(s):
            if c in dic and dic[c] >= start:
                start = dic[c] + 1
                dic[c] = i
            else:
                dic[c] = i
                longest = max(longest,i - start + 1)
        return longest
# @lc code=end

# 判断当前字符是否在dic中，且dic中此串下标大于等于start(代表出现的字符是否在当前字符中,则更新下标为+1


sol = Solution()

print(sol.lengthOfLongestSubstring('abba'))
print(sol.lengthOfLongestSubstring('abcadbacaef'))
print(sol.lengthOfLongestSubstring('abcdcbef'))
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring("dvdf"))

