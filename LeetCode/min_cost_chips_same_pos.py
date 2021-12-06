class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_ct = 0
        evn_ct = 0
        
        for n in position:
            if n % 2 == 0:
                evn_ct += 1
            else:
                odd_ct += 1
        
        return min(evn_ct, odd_ct)
            