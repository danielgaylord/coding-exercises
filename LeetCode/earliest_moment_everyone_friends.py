from collections import defaultdict

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friends = defaultdict(set)
        for person in range(n):
            friends[person].add(person)
        
        logs.sort(key=lambda x: x[0])
        for time, A, B in logs:
            new_friends = friends[A].union(friends[B])
            if len(new_friends) == n:
                return time
            for person in new_friends:
                friends[person] = new_friends
        
        return -1