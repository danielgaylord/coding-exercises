class Solution:
    def longestDupSubstring(self, s: str) -> str:
        size = len(s)

        def longest_substring_of_size(k):
            found = set()
            for i in range(size - k + 1):
                check = s[i:i + k]
                if check in found:
                    return check
                else:
                    found.add(check)
            return None
        
        def binary_search_size():
            left = 0
            right = size
            result = ""
            while left < right:
                mid = (left + right) // 2
                text = longest_substring_of_size(mid)
                if text:
                    result = text
                    left = mid + 1
                else:
                    right = mid
            return result

        return binary_search_size()