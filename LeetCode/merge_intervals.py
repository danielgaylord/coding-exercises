class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals, key=itemgetter(0)))
        results = {}
        prev_start = -1
        for interval in intervals:
            start, end = interval 
            if prev_start > -1 and prev_start <= start <= results[prev_start]:
                results[prev_start] = max(end, results[prev_start])
            else:
                results[start] = end
                prev_start = start
        return list(results.items())