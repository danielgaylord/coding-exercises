# Using splicing
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = len(nums) - k
        nums[:] = nums[shift:] + nums[:shift]

# Using reversing
class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)