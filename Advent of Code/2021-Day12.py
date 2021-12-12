from collections import defaultdict

def passage_pathing(cave_map):
       
    def dfs(cave_map, visited, loc, visited_small):
        new_visited = visited.copy()
        if loc == "end":
            return 1
        if loc.islower():
            if loc in new_visited:
                new_visited[loc] += 1
            else:
                new_visited[loc] = 1

        paths = 0
        for to in cave_map[loc]:
            if to.isupper():
                paths += dfs(cave_map, new_visited, to, visited_small)
            elif to not in new_visited:
                paths += dfs(cave_map, new_visited, to, visited_small)
            elif to in new_visited and new_visited[to] < 2 and not visited_small:
                paths += dfs(cave_map, new_visited, to, True)
        
        return paths

    visited = {}
    return dfs(cave_map, visited, "start", False)

if __name__ == "__main__":
    cave_map = defaultdict(list)
    with open('Advent of Code/2021-Day12.txt', 'r') as input:
        for line in input:
            connection = line.rstrip().split("-")
            if connection[1] != "start" and connection[0] != "end":
                cave_map[connection[0]].append(connection[1])
            if connection[0] != "start" and connection[1] != "end":
                cave_map[connection[1]].append(connection[0])
    
    print(passage_pathing(cave_map))
        