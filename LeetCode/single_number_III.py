from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = defaultdict(int)
        result = []
        for num in nums:
            count[num] += 1
        for key in count:
            if count[key] == 1:
                result.append(count[key])
        return result