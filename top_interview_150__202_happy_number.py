# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        result = n
        while True:
            result = sum([int(digit)*int(digit) for digit in str(result)])
            if result in seen:
                if result == 1:
                    return True
                else:
                    return False
            else:
                seen.add(result)
                print(result)
sol = Solution()
n = 19
print(sol.isHappy(n))
