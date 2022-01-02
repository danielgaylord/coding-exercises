from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        complements = defaultdict(int)
        
        for i, t in enumerate(time):
            temp = t % 60
            if (60 - temp) in complements:
                pairs += complements[60 - temp]
            complements[temp] += 1
            if temp == 0:
                complements[60] += 1
                    
        return pairs