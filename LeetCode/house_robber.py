class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

# improving space from O(n) to O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(a, nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(b, a + nums[i])
        return b