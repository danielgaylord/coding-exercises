class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pt2 = only2 = 1
        
        for pt1 in range(1, len(nums)):
            only2 = (only2 + 1) if nums[pt1] == nums[pt1 - 1] else 1
            if only2 < 3:
                nums[pt2] = nums[pt1]
                pt2 += 1
        return pt2