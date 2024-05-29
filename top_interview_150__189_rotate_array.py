# https://leetcode.com/problems/rotate-array/
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
                
        nums[:] = nums[-k:] + nums[:-k]


sol = Solution()
nums = [1,2]
k = 3
Output = [2,1]
print(nums)
sol.rotate(nums, k)
print(nums)
print("Expected:", Output)
print("#"*32)

nums = [1,2,3,4,5,6,7]
k = 3
Output = [5,6,7,1,2,3,4]
print(nums)
sol.rotate(nums, k)
print(nums)
print("Expected:", Output)
print("#"*32)

nums = [-1,-100,3,99]
k = 2
Output = [3,99,-1,-100]
print(nums)
sol.rotate(nums, k)
print(nums)
print("Expected:", Output)
print("#"*32)