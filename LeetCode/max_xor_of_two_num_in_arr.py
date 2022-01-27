class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_length = len(bin(max(nums))) - 2
        nums = [[(num >> i) & 1 for i in range(max_length)][::-1] for num in nums]
        
        trie = {}
        for num in nums:
            node = trie
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
        
        result = 0
        for num in nums:
            val = ""
            xor = ""
            xnode = trie
            for bit in num:
                val += str(bit)
                if (1 - bit) in xnode:
                    xnode = xnode[1 - bit]
                    xor += str(1 - bit)
                else:
                    xnode = xnode[bit]
                    xor += str(bit)
            xor = int(val, 2) ^ int(xor, 2)
            result = max(result, xor)
                
        return result