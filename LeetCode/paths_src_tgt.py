class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def dfs(graph, ans, path, loc):
            temp = path[:]
            temp.append(loc)
            
            if loc == len(graph) - 1:
                ans.append(temp)
                return
            
            for move in graph[loc]:
                dfs(graph, ans, temp, move)
            
            return
        
        dfs(graph, ans, [], 0)
        return ans
            