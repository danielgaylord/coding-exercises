import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        far_pt = [float('-inf'), (None, None)]
        closest = []
        for _ in range(k):
            closest.append(far_pt)
        heapq.heapify(closest)
        for x, y in points:
            distance = (math.sqrt((x**2) + (y**2)) * -1)
            new = [distance, (x, y)]
            heapq.heappushpop(closest, new)
        result = []
        for distance, point in closest:
            result.append(list(point))
        return result
        