import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        transfers = []
        heapq.heapify(transfers)
        
        for peeps, pickup, dropoff in trips:
            heapq.heappush(transfers, (pickup, peeps))
            heapq.heappush(transfers, (dropoff, -peeps))
        
        
        while transfers:
            location, peeps = heapq.heappop(transfers)
            capacity -= peeps
            if capacity < 0:
                return False
        return True