class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxArr = nums[0]
        minArr = nums[0]
        currMax = maxArr
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxArr, minArr = minArr, maxArr
            
            maxArr = max(nums[i], maxArr * nums[i])
            minArr = min(nums[i], minArr * nums[i])
            currMax = max(currMax, maxArr)

        return currMax
            
            