# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        l = len(str(num))
        roma_dict = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        if len(str(num)) == 4:
            ch = int(str(num)[l-4])
            ans = ans +  'M'* ch
            
        if len(str(num)) >= 3:
            ch = int(str(num)[l-3])
            if ch*100 in roma_dict: 
                ans = ans + roma_dict[ch*100]
            else:
                print(ans,type(ans))
                ans = ans + 'D'*(ch//5) + 'C'*(ch%5)
            
        if len(str(num)) >= 2:
            ch = int(str(num)[l-2])
            if ch*10 in roma_dict: 
                ans = ans + roma_dict[ch*10]
            else:
                ans = ans + 'L'* (ch//5) + 'X'*(ch % 5)
            
        if len(str(num)) >= 1:
            ch = int(str(num)[l-1])
            if ch in roma_dict: 
                ans = ans + roma_dict[ch]
            else:
                ans = ans + 'V'* (ch//5) + 'I'*(ch%5)
        return ans