# Set Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        amount = len(nums)
        inList = set(nums)
        allList = set(i for i in range(1, amount + 1))
        return allList.difference(inList)

# Index Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            nums[num] = -abs(nums[num])
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)   
        return res
