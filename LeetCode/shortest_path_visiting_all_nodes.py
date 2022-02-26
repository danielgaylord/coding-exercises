class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        length = len(graph)
        target = (1 << length) - 1
        queue = [(node, 1 << node) for node in range(length)]
        visited = set(queue)
        
        steps = 0
        while queue:
            temp = []
            for index in rangae(len(queue)):
                node, bmap = queue[index]
                for neighbor in graph[node]:
                    nmap = bmap | (1 << neighbor)
                    if nmap == target:
                        return 1 + steps
                    
                    if (neighbor, nmap) not in visited:
                        visited.add((neighbor, nmap))
                        temp.append((neighbor, nmap))
            
            steps += 1
            queue = temp