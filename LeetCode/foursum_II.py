class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        matches = {}
        
        for A in nums1:
            for B in nums2:
                val = A + B
                if val in matches:
                    matches[val] += 1
                else:
                    matches[val] = 1
        
        for C in nums3:
            for D in nums4:
                val = -(C + D)
                if val in matches:
                    count += matches[val]
                    
        return count