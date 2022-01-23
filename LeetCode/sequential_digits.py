class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_nums = []
        for x in range(1, 10):
            num = x
            for y in range(x + 1, 10):
                num = (num * 10) + y
                seq_nums.append(num)
        seq_nums.sort()
        
        start = 0
        end = len(seq_nums) - 1
        while start < len(seq_nums) and seq_nums[start] < low:
            print(seq_nums[start])
            start += 1
            
        while end >= 0 and seq_nums[end] > high:
            end -= 1
        
        return seq_nums[start:end + 1]