from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        ptr = 0
        p_ct = Counter(p)
        s_ct = Counter()
        
        for index, char in enumerate(s):
            s_ct[char] += 1
            if index >= len(p):
                if s_ct[s[index - len(p)]] == 1:
                    del s_ct[s[index - len(p)]]
                else:
                    s_ct[s[index - len(p)]] -= 1
            if s_ct == p_ct:
                results.append(index - len(p) + 1)
        
        return results