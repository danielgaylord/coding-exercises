class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        sol = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            sol[i] *= pre
            pre *= nums[i]
            sol[len(nums) - i - 1] *= post
            post *= nums[len(nums) - i - 1]
            
        return sol