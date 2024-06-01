# https://leetcode.com/problems/summary-ranges/
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        i = 1
        k = 0
        left = nums[0]
        left_index = 0
        
        n = len(nums)
        ranges = []
        while i < n:
            if nums[i] - nums[i-1] == 1:
                i+=1
                if i == n:
                    print(f"{left=}, {right=}")
                    right = nums[n-1]
                    r = str(left) + "->" + str(right)
                    ranges.append(r)
                    
            else:
                right = nums[i-1]
                if left == right:
                    r = str(left)
                else:
                    r = str(left) + "->" + str(right)
                ranges.append(r)
                left = nums[i]
                k = i
                i+=1
                if i == n:
                    if left - right > 1:
                        ranges.append(str(left))
                    print(f"{left=}, {right=}")
        print(ranges)

sol = Solution()
nums = [0,1,2,4,5,7]
sol.summaryRanges(nums)

nums = [0,2,3,4,6,8,9]
sol.summaryRanges(nums)


"""
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""