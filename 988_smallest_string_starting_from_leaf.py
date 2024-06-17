# for https://leetcode.com/problems/smallest-string-starting-from-leaf/description/

def lexicographical_greatest(left, right):
    """
    lexicographical_greatest("abc", "ab") -> "abc"
    lexicographical_greatest("abc", "abca") -> "abca"
    lexicographical_greatest("ab", "b") -> "b"
    
    """
    if left == right:
        return left
    else:
        if len(left) == len(right):
            for ind in range(len(right)):
                if left[ind] == right[ind]:
                    continue
                if ord(left[ind]) > ord(right[ind]):
                    return left
                else:
                    return right
        else:
            len_of_min = min(len(left), len(right))
            if left[:len_of_min] == right[:len_of_min]:
                