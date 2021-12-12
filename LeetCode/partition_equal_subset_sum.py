class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if n == 1 or total % 2 != 0:
            return False
        
        allow = total // 2
        
        @lru_cache(maxsize=None)
        def dfs(nums, n, target):
            if target == 0:
                return True
            if target < 0 or n == 0:
                return False
            
            return (dfs(nums, n - 1, target) or dfs(nums, n - 1, target - nums[n - 1]))
        
        return dfs(tuple(nums), n - 1, allow)
                
        
        