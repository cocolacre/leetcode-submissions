# https://leetcode.com/problems/132-pattern/

def find132pattern(nums):
    """
    GPT-given working O(n) solution which I am to comprehend.
    """
    stack = []
    s3 = float('-inf')
    for n in reversed(nums):
        if n < s3:
            return True
        while stack and stack[-1] < n:
            s3 = stack.pop()
        stack.append(n)
    return False

