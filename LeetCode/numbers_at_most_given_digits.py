class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        str_num = str(n)
        
        count = 0
        nums = 1
        for x in range(len(str_num) - 1):
            nums *= len(digits)
            count += nums
        
        for i in range(len(str_num)):
            opt = bisect.bisect_left(digits, str_num[i])
            count += (len(digits) ** (len(str_num) - 1 - i)) * opt
            if opt >= len(digits) or digits[opt][0] != str_num[i]:
                return count
        return count + 1