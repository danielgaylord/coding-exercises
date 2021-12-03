class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp = [1 for _ in nums]
        prev = [-1 for _ in nums]
        nums.sort()
        curr_max = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if (dp[j] + 1 > dp[i]):
                        dp[i] = 1 + dp[j]
                        prev[i] = j
            
            if dp[i] > dp[curr_max]:
                curr_max = i
        
        result = []
        while curr_max != -1:
            result.append(nums[curr_max])
            curr_max = prev[curr_max]
        
        result.reverse()
        return result
