class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp = [[] for _ in nums]
        nums.sort()
        result = []

        for i in range(n):
            dp[i] = []
            for j in range(i):
                if (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0) and len(dp[i]) < len(dp[j]):
                    dp[i] = dp[j]
            dp[i].append(nums[i])

            
            if len(dp[i]) > len(result):
                result = dp[i]
        
        return result
