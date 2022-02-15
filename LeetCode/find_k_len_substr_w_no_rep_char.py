from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        chars = Counter(s[:k])
        subs = 0
        length = len(s)
        
        for index in range(k, length):
            if len(set(chars)) == k:
                subs += 1
            old_char = s[index - k]
            new_char = s[index]
            chars[old_char] -= 1
            if chars[old_char] <= 0:
                del chars[old_char]
            chars[new_char] += 1
        if len(set(chars)) == k:
                subs += 1
        
        return subs