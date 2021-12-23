from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        edges = defaultdict(int)
        
        for order in prerequisites:
            graph[order[1]].append(order[0])
            edges[order[0]] += 1
            
        options = []
        order = []
        for i in range(numCourses):
            if i not in edges:
                options.append(i)
                
        while options:
            course = options.pop()
            order.append(course)
            for val in graph[course]:
                edges[val] -= 1
                if edges[val] == 0:
                    options.append(val)
        
        if len(order) == numCourses:
            return order
        else:
            return []