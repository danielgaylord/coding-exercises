from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vals = defaultdict(int)
        max_num = 0
        for num in nums:
            vals[num] += num
            max_num = max(max_num, num)
            
        dp = [0 for _ in range(max_num + 1)]
        dp[1] = vals[1]
        
        for num in range(2, len(dp)):
            dp[num] = max(dp[num - 1], dp[num - 2] + vals[num])
        return dp[max_num]