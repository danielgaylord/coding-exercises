class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) % 2 == 0:
            return -1
        for index in range(0, len(nums), 2):
            if index == len(nums) - 1:
                return nums[index]
            if nums[index] != nums[index + 1]:
                return nums[index]
        return -1
        