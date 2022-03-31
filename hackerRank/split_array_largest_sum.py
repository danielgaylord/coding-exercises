class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        length = len(nums)
        dp = [[0] * (m + 1) for _ in range(length)]
        
        prefix = [0] + list(itertools.accumulate(nums))
        
        for sub_ct in range(1, m + 1):
            for curr_index in range(length):
                if sub_ct == 1:
                    dp[curr_index][sub_ct] = prefix[length] - prefix[curr_index]
                    continue
                min_split = prefix[length]
                for i in range(curr_index, length - sub_ct + 1):
                    first_split = prefix[i + 1] - prefix[curr_index]
                    largest_split = max(first_split, dp[i + 1][sub_ct - 1])
                    min_split = min(min_split, largest_split)
                    
                    if first_split >= min_split:
                        break
                
                dp[curr_index][sub_ct] = min_split
        
        return dp[0][m]