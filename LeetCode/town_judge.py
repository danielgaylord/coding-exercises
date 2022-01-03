#Using hashmaps
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(list)
        trusted = defaultdict(list)
        
        for a, b in trust:
            trusts[a].append(b)
            trusted[b].append(a)
        
        for person in range(1, n + 1):
            if person not in trusts and len(trusted[person]) == n - 1:
                return person
        return -1

#Using single array
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_meter = [0 for _ in range(n)]
        
        for a, b in trust:
            trust_meter[a - 1] -= 1
            trust_meter[b - 1] += 1
        
        for person, value in enumerate(trust_meter):
            if value == n - 1:
                return person + 1
        return -1