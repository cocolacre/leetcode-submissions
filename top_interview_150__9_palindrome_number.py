#https://leetcode.com/problems/palindrome-number/
import typing

class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        n = len(str(x))
        s = str(x)
        i = 0
        while i <= n / 2:
            print(f"{i=} {s[i]=} {n-i-1=} {s[n-i-1]=}")
            if s[i] == s[n-i-1]:
                i+=1
                continue
            else:
                print(False)
                return False
        print(x)
        print(True)
        return True
        
s = Solution()
x = 121
s.isPalindrome(x)

x = 1221
s.isPalindrome(x)
x = 11
s.isPalindrome(x)
x = 1
s.isPalindrome(x)
x = 10
s.isPalindrome(x)
x = 110
s.isPalindrome(x)