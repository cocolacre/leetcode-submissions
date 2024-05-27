# https://leetcode.com/problems/max-points-on-a-line/
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        max_points_on_line = 0
        for ind1, p1 in enumerate(points[:len(points)-1]):
            for p2 in points[ind1+1:]:
                if p2[0]!=p1[0]:
                    k = (p2[1] - p1[1])/(p2[0]-p1[0])
                    b = -p1[0]*k + p1[1]
                    num_points_on_this_line = 0
                    for p3 in points:
                        if abs((p3[1] - k*p3[0] - b))<0.00000000001:
                            #print(p3[0],p3[1],k,b )
                            num_points_on_this_line += 1
                    #print(f"{num_points_on_this_line=}")
                    if num_points_on_this_line > max_points_on_line:
                        max_points_on_line = num_points_on_this_line
                else:
                    num_points_on_this_line =0
                    for p3 in points:
                        if p3 != p1 and p3 != p2:
                            if p3[0]==p1[0]:
                                num_points_on_this_line += 1
                    num_points_on_this_line +=2
                    print(num_points_on_this_line)
                    if num_points_on_this_line > max_points_on_line:
                        max_points_on_line = num_points_on_this_line
                    
        return max_points_on_line