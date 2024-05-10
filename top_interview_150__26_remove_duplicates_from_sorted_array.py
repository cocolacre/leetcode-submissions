#remove-duplicates-from-sorted-array

from typing import List
import pytest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = 0
        k = 0
        
        max_element = nums[-1]
        n = len(nums)
        if n == 1:
            return 1
        left = 0
        right = 1
        while True:
            print(f"[1]{left=} {nums[left]=} {right=} {nums[right]=}")
            print(f"[1]{nums=}")
            if nums[left] == nums[right]:
                right += 1
                if right == n:
                    return left + 1
            elif nums[left] < nums[right]:
                if right - left == 1:
                    # nums[left] and nums[right] are two consequtive unique numbers, shift 2 pointers right.
                    left+=1
                    right+=1
                    if right == n:
                        return left + 1
                else:
                    left += 1
                    nums[left] = nums[right]
                    right += 1
                    if right == n:
                        return left + 1
            print(f"[1]{left=} {nums[left]=} {right=} {nums[right]=}")
            print(f"[1]{nums=}")
if __name__ == "__main__":

    s = Solution()

    nums = [0,0,1,2,2,3,4,4,4,5]
    k = s.removeDuplicates(nums)
    print("RESULT:", k, nums[:k])


    nums = [0,0]
    k = s.removeDuplicates(nums)
    print("RESULT:", k, nums[:k])

    nums = [0,0,0,0,1]
    k = s.removeDuplicates(nums)
    print("RESULT:", k, nums[:k])

    nums = [-99,-99, -50, -40, -40, -30, -20,-20,-20,-20, -10,-10, -5,0,0,0,0,1]
    k = s.removeDuplicates(nums)
    print("RESULT:", k, nums[:k])


    nums = [-100, -99, -99, -99, -98, -97, -95, -95, -93, -92, -90, -90, -90, -89, -89, -89, -88, -87, -86, -86, -84, -83, -82, -82, -80, -80, -77, -77, -76, -75, -73, -73, -73, -71, -68, -66, -65, -62, -62, -58, -55, -54, -53, -53, -52, -51, -50, -50, -50, -49, -48, -47, -47, -46, -44, -43, -41, -41, -37, -34, -32, -32, -31, -30, -29, -28, -23, -23, -22, -22, -20, -17, -17, -17, -14, -14, -13, -12, -12, -12, -11, -10, -10, -9, -9, -9, -9, -8, -6, -6, -5, -5, -4, -4, -4, -4, -3, -2, -1, -1, -1, 1, 2, 3, 3, 5, 7, 10, 10, 12, 12, 12, 13, 14, 17, 17, 17, 18, 19, 19, 19, 19, 22, 22, 25, 27, 29, 32, 32, 33, 35, 37, 40, 40, 41, 41, 42, 44, 46, 46, 47, 47, 48, 49, 49, 49, 50, 52, 52, 52, 53, 54, 56, 56, 56, 57, 58, 59, 59, 60, 61, 61, 62, 63, 64, 65, 66, 66, 67, 67, 69, 70, 70, 71, 72, 72, 72, 72, 73, 74, 76, 77, 77, 79, 81, 84, 85, 85, 85, 87, 87, 89, 89, 90, 91, 94, 94, 94, 95, 98]
    k = s.removeDuplicates(nums)
    print("RESULT:", k, nums[:k])

    info = """
[0,0,1,2,2,3,4,4,4,5]
 ^
   ^
equals? yes, increment i1 and i2? NO, increment i2
[0,0,1,2,2,3,4,4,4,5]
 ^
     ^
equals? no. so nums[i1]!=nums[i2], i1=0, i2=2?
    i2-i1==1? then increment i1 and i2
    i2-i1>1? then swap nums[i1+1] and nums[i2], then i1++, and i2++
    




[0,0,1,2,2,3,4,4,4,5] WRONG
   ^
     ^
[0,1,0,2,2,3,4,4,4,5] WRONG
   ^
     ^
[0,1,0,2,2,3,4,4,4,5] WRONG
     ^
       ^
[0,1,2,0,2,3,4,4,4,5]
     ^
       ^
[0,1,2,0,2,3,4,4,4,5]
     ^
         ^
[0,1,2,0,2,3,4,4,4,5]
     ^
           ^
[0,1,2,0,2,3,4,4,4,5]
       ^
           ^
[0,1,2,3,2,2,4,4,4,5]
       ^
           ^
[0,1,2,3,2,2,4,4,4,5]
       ^   (cmp)
             ^
[0,1,2,3,2,2,4,4,4,5]
         ^ (inc)
             ^
[0,1,2,3,4,2,2,4,4,5]
         ^ (swp)
             ^
[0,1,2,3,4,2,2,4,4,5]
         ^
               ^(inc,cmp)
[0,1,2,3,4,2,2,4,4,5]
         ^
                 ^(inc,cmp)
[0,1,2,3,4,2,2,4,4,5]
         ^
                   ^(inc,cmp)

[0,1,2,3,4,2,2,4,4,5]
           ^(inc,swp)
           
[0,1,2,3,4,5,2,4,4,2]
           ^(inc,swp)
                   ^

[0,0,1,2,2,3,4,4,4,5]


[0,0,1,2,2,3,4,4,4,5]


[0,0,1,2,2,3,4,4,4,5]


[0,0,1,2,2,3,4,4,4,5]


[0,0,1,2,2,3,4,4,4,5]

"""