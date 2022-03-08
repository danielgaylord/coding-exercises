class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        pairs = [["0", "0"], ["1", "1"], ["6", "9"], ["8", "8"], ["9", "6"]]
        
        def strobHelper(n, length):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            prev = strobHelper(n - 2, length)
            new = []

            for num in prev:
                for pair in pairs:
                    if pair[0] != "0" or n != length:
                        new.append(pair[0] + num + pair[1])

            return new
        
        return strobHelper(n, n)