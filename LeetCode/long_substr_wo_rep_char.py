class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        low = 1
        high = length
        mid = (low + high) // 2
        longest = 0

        if length < 2:
            return length

        def subTest(midTest):
            for start in range(length - midTest + 1):
                substr = s[start:start + midTest]
                if len(set(substr)) == len(substr):
                    return True
            return False
        
        while low <= high:
            if subTest(mid):
                longest = mid
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return longest