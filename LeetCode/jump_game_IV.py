from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int: 
        values = defaultdict(list)
        for index, val in enumerate(arr):
            values[val].append(index)
        
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append((0, 0))
        
        while queue:
            loc, steps = queue.popleft()
            if loc == len(arr) - 1:
                return steps
            if loc - 1 >= 0 and (loc - 1) not in visited:
                queue.append((loc - 1, steps + 1))
                visited.add(loc - 1)
            if loc + 1 < len(arr) and (loc + 1) not in visited:
                queue.append((loc + 1, steps + 1))
                visited.add(loc + 1)
            if arr[loc] in values:
                for poss in values[arr[loc]]:
                    if poss not in visited:
                        queue.append((poss, steps + 1))
                        visited.add(poss)
                values[arr[loc]].clear()
        return -1
                