class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0
        for index in range(len(nums)):
            for dist in range(1, nums[index] + 1):
                land = index + dist
                if land < len(nums):
                    dp[land] = min(dp[land], dp[index] + 1)
        return dp[-1]