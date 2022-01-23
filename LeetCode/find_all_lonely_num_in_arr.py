from collections import defaultdict

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        result = []
        
        for num in nums:
            counts[num] += 1
        
        for key, value in counts.items():
            if value == 1 and key - 1 not in counts and key + 1 not in counts:
                result.append(key)
        
        return result