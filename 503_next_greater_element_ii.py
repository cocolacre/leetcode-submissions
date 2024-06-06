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


class SolutionLexa2:
    """
    2 stacks - one with elements, other with their indicies.
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = max(nums)
        ms = []
        msind = []

        answer = [-1]* len(nums)

        ind_max = nums.index(m)
        l = len(nums) 


        for i in range(l+1):

            elem = nums[ (i + ind_max)%l ]
            counter_del = 0 
            while ms and elem > ms[-1]:

                answer[ msind[-1] ] = elem
                ms.pop()
                msind.pop()

            ms.append(elem)
            msind.append((i + ind_max)%l)
            
        return answer

#TODO: my solution.
