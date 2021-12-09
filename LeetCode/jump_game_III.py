from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        visited = [False] * len(arr)
        
        while queue:
            loc = queue.popleft()
            visited[loc] = True
            if arr[loc] == 0:
                return True
            jump_left = loc - arr[loc]
            jump_right = loc + arr[loc]
            if 0 <= jump_left and not visited[jump_left]:
                queue.append(jump_left)
            if jump_right < len(arr) and not visited[jump_right]:
                queue.append(jump_right)
        return False