class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda elem: elem[1])
        
        curr_end = float('-inf')
        arrows = 0
        
        for x_start, x_end in points:
            if x_start > curr_end:
                arrows += 1
                curr_end = x_end
        
        return arrows