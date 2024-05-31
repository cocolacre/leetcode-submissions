# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        O(n^2) wrong solution.
        """
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(i+1, i+k+1):
                print(f"{i=}, {j=}, {k=}")
                if j >= n:
                    continue
                if nums[i] == nums[j]:
                    print(f"{i=}, {j=}, {k=}")
                    if abs(i-j) <=k:
                        return True
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums_indexes = {}
        for i, num in enumerate(nums):
            if num not in nums_indexes:
                nums_indexes[num] = i
            else:
                if abs(i - nums_indexes[num]) <= k:
                    return True
                else:
                    nums_indexes[num] = i
        return False

sol = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums, k))

nums = [1,2,3,4,5,6,7,8,9,9]
k = 3
print(sol.containsNearbyDuplicate(nums, k))