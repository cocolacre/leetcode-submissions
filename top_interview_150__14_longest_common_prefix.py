# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        words = strs[1:]
        first = strs[0]
        i = 0
        prefix = ""
        while True:
            print(f"{i=}")
            for word in words:
                if word[:i] != first[:i]:
                    return prefix
            for word in words:
                if len(word) == i or len(first) == i or len(word) == 0 or len(first) == 0:
                    print(f"[2]{first[:i]=}    {word[:i]=}")
                    prefix = first[:i]
                    return prefix
            prefix = first[:i]
            i+=1



sol = Solution()


strs = ["dog","racecar","car"]
print("RESULT:", sol.longestCommonPrefix(strs))

strs = ["flower","flow","flight"]
print("RESULT:", sol.longestCommonPrefix(strs))

strs = ["ab", "a"]
print("RESULT:", sol.longestCommonPrefix(strs))

strs = ["a","b"]
print("RESULT:", sol.longestCommonPrefix(strs))

strs = ["a","a","b"]
print("RESULT:", sol.longestCommonPrefix(strs))