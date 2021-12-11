import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        low = 0
        high = n * min(a, b)
        mod = (10 ** 9) + 7
        lcd = a // math.gcd(a, b) * b
        
        while low < high:
            mid = (low + high) // 2
            if mid // a + mid // b - mid // lcd < n:
                low = mid + 1
            else:
                high = mid
        return low % mod
        