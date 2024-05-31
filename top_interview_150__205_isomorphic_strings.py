# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t_map = {}
        mapped_t_chars = set()
        for ind, char in enumerate(s):
            if char not in s2t_map:
                s2t_map[char] = t[ind]
                #t2s_map[t[ind]] = char
                if t[ind] in mapped_t_chars:
                    return False
                else:
                    mapped_t_chars.add(t[ind])
            else:
                if s2t_map[char] != t[ind]:
                    return False
        return True