import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        
        for start, end in intervals[1:]:
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        
        return len(rooms)
            