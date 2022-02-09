class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        opts = {}
        
        for num in nums:
            if num in opts:
                opts[num] += 1
            else:
                opts[num] = 1
        print(opts)
        results = 0
        for key in opts.keys():
            if k > 0 and key + k in opts:
                results += 1
            elif k == 0 and opts[key] > 1:
                results += 1
            
        return results