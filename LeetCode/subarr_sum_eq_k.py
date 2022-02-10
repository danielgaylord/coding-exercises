class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = total = 0
        sum_counts = {0: 1}
        for num in nums:
            total += num
            if total - k in sum_counts:
                count += sum_counts[total - k]
            if total in sum_counts:
                sum_counts[total] += 1
            else:
                sum_counts[total] = 1
        return count