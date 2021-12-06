class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=itemgetter(0))
        ints = {}
        prev_start = -1
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if prev_start > -1:
                if prev_start <= start <= ints[prev_start]:
                    ints[prev_start] = max(end, ints[prev_start])
                    start = prev_start
                else:
                    ints[start] = end
            else:
                ints[start] = end
            prev_start = start
        return list(ints.items())