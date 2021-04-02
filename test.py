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

sol = Solution()
print(sol.reverse(1463847412))