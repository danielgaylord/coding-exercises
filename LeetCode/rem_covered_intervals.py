class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        covered = 0
        
        prev = 0
        for start, end in intervals:
            if end > prev:
                covered += 1
                prev = end
        
        return covered