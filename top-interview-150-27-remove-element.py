# top-interview-150-27-remove-element.py
# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print(f"{nums=} {val=}")
        m = 0
        i = 0
        tmp = 0
        n = len(nums)
        while i < n - m:
            print(f"{i=} {n-m=} {nums[i]=}")
            if nums[i] == val:
                if i == n-1:
                    return i
                while nums[n-m-1] == val:
                    print(f"[1]{i=} {n-m-1=}")
                    if n-m-1 == 0:
                        return 0
                    if n-m-1 == i:
                        return i
                    print(f"[2]{i=} {n-m-1=}")
                    m+=1
                tmp = nums[n-m-1]
                nums[n-m-1] = val
                nums[i] = tmp
                m+=1
            i+=1
            print(nums)
        k = n - m
        print("RESULT k = " + str(k))
        return k
s = Solution()
re = s.removeElement

nums = [3,2,2,3]
val = 3
print(re(nums, val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(re(nums, val))

nums = [4,5]
val = 5
print(re(nums, val))

nums = [1]
val = 1
print(re(nums, val))

nums = [11,11,11]
val = 11
print(re(nums, val))


nums = [2,2,3]
val = 2
print(re(nums, val))
