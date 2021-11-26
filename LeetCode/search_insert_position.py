class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        
        while low < high:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = min(len(nums) - 1, mid + 1)
            else:
                high = max(0, mid - 1)
            mid = (low + high) // 2
        if nums[mid] < target:
            return mid + 1
        else:
            return mid