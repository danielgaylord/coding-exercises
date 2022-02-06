import heapq

class Solution:
    def smallestNumber(self, num: int) -> int:
        digstr = str(num)
        neg = False
        count0 = 0
        if digstr[0] == "-":
            neg = True
            digits = [(-1 * int(char)) for char in digstr[1:]]
        else:
            digits = [int(char) for char in digstr]
        for index, digit in enumerate(digits):
            if digit == 0:
                count0 += 1
        heapq.heapify(digits)
        result = 0
        while digits:
            digit = heapq.heappop(digits)
            if digit == 0:
                continue                   
            else:
                result *= 10      
                result += abs(digit)
                if not neg:
                    for _ in range(count0):
                            result *= 10
                    count0 = 0
        
        if neg:
            for _ in range(count0):
                result *= 10
        
        return result if not neg else (-1 * result)
            