# https://leetcode.com/problems/merge-sorted-array/?source=submission-ac

def merge(nums1, m, nums2, n):
    if n == 0:
        print(nums1)
        return
    if m == 0:
        nums1[:] = nums2[:]
        print(nums1)
        return
    nums1[:] = nums1[:m]
    nums1_max = max(nums1)
    i1 = 0
    i2 = 0
    while i1 < n+m and i2 < n:
        if i1 == len(nums1):
            nums1.extend(nums2[i2:])
            print(nums1)
            return
        if nums1[i1] == nums2[i2]:
            nums1.insert(i1, nums2[i2])
            i1+=2
            i2+=1
        elif nums1[i1] < nums2[i2]:
            i1+=1
        elif nums1[i1] > nums2[i2]:
            nums1.insert(i1, nums2[i2])
            i1+=1
            i2+=1
    print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
merge(nums1, m, nums2, n)

nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 1
nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
n = 90
merge(nums1, m, nums2, n)
