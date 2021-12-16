from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]
        
        adj_list = defaultdict(list)
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        
        queue = deque()
        for x in range(n):
            if len(adj_list[x]) == 1:
                queue.append(x)

        nodes_left = n
        while nodes_left > 2:
            nodes_left -= len(queue)
            temp = deque()
            while queue:
                node = queue.popleft()
                rel = adj_list[node].pop()
                del adj_list[node]
                adj_list[rel].remove(node)
                if len(adj_list[rel]) == 1:
                    temp.append(rel)
            queue = temp
        
        return queue
                