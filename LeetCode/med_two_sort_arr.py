class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:      
        while len(nums1) + len(nums2) > 2:
            if not nums1:
                nums2 = nums2[1:-1]
            elif not nums2:
                nums1 = nums1[1:-1]
            else:
                if nums1[0] < nums2[0]:
                    nums1 = nums1[1:]
                else:
                    nums2 = nums2[1:]
                
                if not nums1:
                    nums2 = nums2[:-1]
                elif not nums2:
                    nums1 = nums1[:-1]
                elif nums1[-1] > nums2[-1]:
                    nums1 = nums1[:-1]
                else:
                    nums2 = nums2[:-1]
        
        total = sum(nums1) + sum(nums2)
        length = len(nums1) + len(nums2)
            
        return float(total / length)
        