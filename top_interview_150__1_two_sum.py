from typing import List

# https://leetcode.com/problems/two-sum/
# Beats 84.25% of users with Python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = 0
        while left < n - 1:
            right = left + 1
            print(f"[2]{left=} {nums[left]=} {right=} {nums[right]=}")
            while right < n:
                if nums[left] + nums[right] == target:
                    return [left, right]
                right += 1
            left+=1


s = Solution()

nums = [2,7,11,15]
target = 9
print(s.twoSum(nums,target))

nums = [3,2,4]
target = 6
print(s.twoSum(nums,target))

nums = [3,3]
target = 6
print(s.twoSum(nums,target))