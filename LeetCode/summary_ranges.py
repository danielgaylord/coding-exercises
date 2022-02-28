class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        prev = float('-inf')
        prev_start = float('-inf')
        temp = ""
        nums.append(float('inf'))
        
        for num in nums:
            if num != prev + 1:
                if prev == prev_start:
                    ranges.append(temp)
                else:
                    ranges.append(temp + "->" + str(prev))
                temp = str(num)
                prev_start = num
            prev = num
        
            
        return ranges[1:]