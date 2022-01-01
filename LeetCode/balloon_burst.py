class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @lru_cache(maxsize=None)
        def dfs(left, right):
            if right - left < 0:
                return 0
            result = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                balloons = dfs(left, i - 1) + dfs(i + 1, right)
                result = max(result, balloons + coins)
            return result
        return dfs(1, len(nums) - 2)
            