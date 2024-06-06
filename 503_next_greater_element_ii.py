# https://leetcode.com/problems/next-greater-element-ii/
from typing import List

class SolutionLeha:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = max(nums)
        ms = []
        answer = [-1]* len(nums)
        ind_max = nums.index(m)
        l = len(nums) 

        nwi = []
        for i,el in enumerate(nums):
            nwi.append([i,el])


        for i in range(l+1):
            elem = nwi[ (i + ind_max)%l ]
            while ms and elem[1] > ms[-1][1]:
                answer[ms[-1][0]] = elem[1]
                ms.pop()
            ms.append(elem)
        return answer
#TODO: my solution.