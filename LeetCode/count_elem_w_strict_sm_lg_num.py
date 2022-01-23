class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        low = nums[0]
        high = nums[-1]
        if low == high:
            return 0
        
        li = 0
        hi = len(nums) - 1
        
        while li < len(nums) and nums[li] == low:
            li += 1
        
        while hi >= 0 and nums[hi] == high:
            hi -= 1
        
        if li > hi:
            return 0
        
        return len(nums[li:hi + 1])
        