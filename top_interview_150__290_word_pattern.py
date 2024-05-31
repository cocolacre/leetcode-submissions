# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_2_words_map = {}
        mapped_words = set()
        words = [word for word in s.split(" ")]
        if len(words) != len(pattern):
            return False
        for ind, letter in enumerate(pattern):
            if letter not in pattern_2_words_map:
                pattern_2_words_map[letter] = words[ind]
                if words[ind] in mapped_words:
                    return False
                else:
                    mapped_words.add(words[ind])
            else:
                if pattern_2_words_map[letter] != words[ind]:
                    return False
        return True