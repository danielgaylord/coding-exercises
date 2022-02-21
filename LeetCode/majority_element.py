from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = Counter(nums)
        
        return times.most_common(1)[0][0]