class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        curr = prev = total = 0
        
        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                curr = prev + 1
                total += curr
            else:
                curr = 0
            prev = curr
        
        return total