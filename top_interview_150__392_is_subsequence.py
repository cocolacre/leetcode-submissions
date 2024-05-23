#https://leetcode.com/problems/is-subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        k = 0
        len_s = len(s)
        len_t = len(t)
        if s == "":
            return True
        while i < len_s and k < len_t:
            print(f"{i=} {s[i]=} {k=} {t[k]=}")
            if s[i] == t[k]:
                if i == len_s - 1:
                    print(True)
                    return True
                i+=1
                k+=1
            else:
                k+=1
        print(False)
        return False


sol = Solution()


s = "abc"
t = "ahbgdc"
print(s, t, sol.isSubsequence(s,t))

s = "axc"
t = "ahbgdc"
print(s, t, sol.isSubsequence(s,t))

s = "acb"
t = "ahbgdc"
print(s, t, sol.isSubsequence(s,t))

"abc"
"ahbgdc"

"abc"
"ahbgdc"