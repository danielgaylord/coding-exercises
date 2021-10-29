class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in holder:
                return [holder[diff], index]
            else:
                holder[nums[index]] = index
        return None