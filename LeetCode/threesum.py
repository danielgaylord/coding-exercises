class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        targets, keys = set(), set()

        nums.sort()
        for index, target in enumerate(nums):
            if target in targets:
                continue
            targets.add(target)
            
            low = index + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] + target == 0:
                    key = str(target) + "," + str(nums[low]) + "," + str(nums[high])
                    if key not in keys:
                        keys.add(key)
                        result.append([target, nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] + target < 0:
                    low += 1
                elif nums[low] + nums[high] + target > 0:
                    high -= 1
        return result