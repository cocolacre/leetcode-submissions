from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        i = 0
        k = 0
        counter1 = {}
        n = len(nums)
        
        for item in nums:
            if item in counter1:
                counter1[item] = counter1[item] + 1
            else:
                counter1[item] = 1
            #print(f"{left=}, {i=},{cnt[left]=}, {k=}, {right=} ")
            #print(f"{left=}, {i=},{cnt[left]=}, {k=}, {right=} \n" + "#"*30)
        items = list(counter1.keys())
        m = len(items)
        print(items)
        print(counter1)
        while k < m:
            if counter1[items[k]] == 1:
                nums[i] = items[k]
                i+=1
                k+=1
            else:
                nums[i] = items[k]
                i+=1
                nums[i] = items[k]
                i+=1
                k+=1
        print(nums)
               
sol = Solution() 
nums = [1,1,1,2,2,3]
sol.removeDuplicates(nums)

nums = [1,1,1,1,2,2,3]
sol.removeDuplicates(nums)
nums = [1,2,2,2,2,3,4,4,4,5,5,5,6,8]
sol.removeDuplicates(nums)

"""

[1,1,1,2,2,3]
 ^ ^
cnt=1
cmp: left == right => inc
[1,1,1,2,2,3]
   ^ ^
cnt=2
cmp: left == right
    We need to increment k until a bigger integer appears
[1,1,1,2,2,3]
   ^   ^
cnt = 2
cmp: left < right
increment i, swap, increment k
[1,1,1,2,2,3]
     ^ ^
[1,1,2,2,2,3]
     ^ ^
[1,1,2,2,2,3]
     ^   ^




[1,1,1,2,2,3]
   k i

[1,1,1,2,2,3]
   k   i
[1,1,1,2,2,3]
   k   i
   
   
   
"""