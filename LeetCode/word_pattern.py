class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        words = s.split(" ")
        match = {}
        used = set()
        
        if len(pattern) != len(words):
            return False
        
        for p, word in zip(pattern, words):
            if p not in match:
                if word in used:
                    return False
                match[p] = word
                used.add(word)
            elif match[p] != word:
                return False
        return True