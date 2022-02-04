class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0: -1}
        maxlen = count = 0
        
        for index, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in counts:
                maxlen = max(maxlen, index - counts[count])
            else:
                counts[count] = index
        
        return maxlen