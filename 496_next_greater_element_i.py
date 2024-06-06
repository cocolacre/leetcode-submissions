# https://leetcode.com/problems/next-greater-element-i
from typing import List

class SolutionLeha:
    # grinya-made solution on 07.07 at 00:00.
    # uses monotonic decreasing stack ("срезаем гребни")
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ms = []
        answer = []
        for a in nums2:
            if ms == []:
                ms.append(a)
            elif a <= ms[-1]:
                ms.append(a)
            else:
                while ms and a > ms[-1]:
                    d[ms[-1]] = a
                    ms.pop()
                ms.append(a)

        for a in nums1:
            if a in d:
                answer.append( d[a] )
            else:
                answer.append(-1)
                
        return answer


class SolutionLeha2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ms = []
        for a in nums2:
            while ms and a > ms[-1]:
                d[ms.pop()] = a
            ms.append(a)
        return [d.get(num,-1) for num in nums1]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []



nums = [1,5,2,43,1,433,23,2,55,1,5,8,6,9,12,11,10,14,1,2,1,54,6,0,1,5,3,2,6,53]

nums = [1,4,2,5]
expected = [4,5,5,5]
infos = """
add 1 to stack: [1]
try adding 4 to decreasing stack: [1]. but we can not, we must pop the "1" from it first.
pop 1 from stack.
add 4 to stack. also 4 is next greater element for 1.
now stack is [4,]


"""
def find_next_greater_elements(nums):
    """
    For each element in nums, find the next greater element for it and return an 
    array of such <greater> corresponding elements, or the elements itself if greater
    was not found.
    
    """
    
    stack = []
    results = []
    mapping = {}
    for num in nums:
        while stack and num > stack[-1]:
            stack.pop()
        