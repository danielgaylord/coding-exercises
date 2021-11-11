class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        startVal = 1
        foundNeg = False
        for index in range(len(nums) - 1, -1, -1):
            if not foundNeg and nums[index] < 0:
                foundNeg = True
            if foundNeg:
                startVal -= nums[index]
            if startVal < 1:
                startVal = 1
        return startVal