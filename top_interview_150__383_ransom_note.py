# https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = {}
        ransom_note_counter = {}
        for letter in magazine:
            if letter not in magazine_counter:
                magazine_counter[letter] = 1
            else:
                magazine_counter[letter] = magazine_counter[letter] + 1
        
        for letter in ransomNote:
            if letter not in ransom_note_counter:
                ransom_note_counter[letter] = 1
            else:
                ransom_note_counter[letter] = ransom_note_counter[letter] + 1

        for letter in ransomNote:
            if letter not in magazine_counter:
                return False
            elif ransom_note_counter[letter] > magazine_counter[letter]:
                 return False
        return True