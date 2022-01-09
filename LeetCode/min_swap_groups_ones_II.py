class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if sum(nums) == 0 or sum(nums) == len(nums):
            return 0
            
        total = sum(nums)
        length = len(nums)
        nums.extend(nums)
        
        max_wind = subtotal = sum(nums[0:total])
        for x in range(1, length):
            subtotal -= nums[x - 1]
            subtotal += nums[x + total - 1]
            max_wind = max(max_wind, subtotal)
        return total - max_wind