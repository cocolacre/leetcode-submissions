# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = "".join([ch for ch in s if ch.isalnum()])
        print(a)
        n = len(a)
        i = 0
        if len(a) == 1:
        while i < n/2:
            if a[i] == a[n-i-1]:
                i+=1
                continue
            else:
                print(False)
                return False
        print(True)
        return True


s = Solution()
x = "A man, a plan, a canal: Panama"
s.isPalindrome(x)

x = "aA man, a plan, a canal: Panamaa"
s.isPalindrome(x)

x = "A man, a plan, a canal: Panamaa"
s.isPalindrome(x)

x = "A man, a plan, a canal: Panama"
s.isPalindrome(x)