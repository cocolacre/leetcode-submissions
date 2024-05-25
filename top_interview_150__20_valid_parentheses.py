# https://leetcode.com/problems/valid-parentheses/

class WrongSolution:
    def isValid(self, s: str) -> bool:
        """
        '(', ')', '{', '}', '[' and ']'
        """
        par_counter = 0
        par_open = False
        
        curly_counter = 0
        curly_open = False
        
        rect_counter = 0
        rect_open = False
        
        for ch in s:
            if ch == "[":
                rect_counter += 1
                rect_open = True
            if ch == "]":
                rect_counter -= 1
                rect_open = False
            if ch == "(":
                par_counter += 1
                par_open = True
            if ch == ")":
                par_counter -= 1    
                par_open = False
            if ch == "{":
                curly_counter += 1
                curly_open = True
            if ch == "}":
                curly_counter -= 1
                curly_open = False
            
                
        return not par_counter and not par_open and not rect_counter and not rect_open and not curly_counter and not curly_open


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or \
                    (ch == ")" and stack[-1] != "(") or (ch == "]" and stack[-1] != "[") or (ch == "}" and stack[-1] != "{"):
                    return False
                stack.pop()
        return not stack             


sol = Solution()
s = "{}[][]()"
print(s, sol.isValid(s))

s = "{}[][]())"
print(s, sol.isValid(s))

s = "{}[]][())"
print(s, sol.isValid(s))

s = "([)]"
print(s, sol.isValid(s))