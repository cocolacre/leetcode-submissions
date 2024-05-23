# https://leetcode.com/problems/majority-element/
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        n = len(nums)
        print(nums)
        if n == 1:
            return nums[0]
        for key in nums:
            if key not in d:
                d[key] = 1
            else:
                d[key] = d[key] + 1
                if d[key] > n/2:
                    return key
        
        
        
        
s = Solution()
nums = [3,2,3]
print(s.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))

nums = [1]
print(s.majorityElement(nums))
