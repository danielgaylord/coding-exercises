class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = [float('inf') for _ in range(len(seats))]
        for index, full in enumerate(seats):
            if full:
                distance[index] = 0
            elif index > 0 and distance[index - 1] != float('inf'):
                distance[index] = distance[index - 1] + 1 
        
        for index, full in reversed(list(enumerate(seats))):
            if full:
                distance[index] = 0
            elif index < len(seats) - 1:
                distance[index] = min(distance[index], distance[index + 1] + 1)
        
        return max(distance)