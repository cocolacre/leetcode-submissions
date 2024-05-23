# https://leetcode.com/problems/length-of-last-word
import typing

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [word for word s.split(" ") if word != ""]
        last = words[-1]
        return len(last)


sol = Solution()
s = "Hello World"
print(sol.lengthOfLastWord(s))

