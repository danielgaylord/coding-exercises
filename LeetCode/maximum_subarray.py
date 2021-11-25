class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        maxsum = dp
        
        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            maxsum = max(maxsum, dp)
            
        return maxsum
        