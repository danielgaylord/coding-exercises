#DIDN'T WORK...NEED TO DO DP...

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        low = 1
        high = len(s)
        mid = (low + high) // 2
        result = ""

        if s == s[::-1]:
            return s

        def substrTest(string, point):
            for index in range(len(string) - point + 1):
                substring = string[index : index + point]
                if substring == substring[::-1]:
                    return substring
            return None

        while low <= high:
            hold = substrTest(s, mid)
            if hold:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
            if hold and len(hold) > len(result):
                    result = hold
        return result