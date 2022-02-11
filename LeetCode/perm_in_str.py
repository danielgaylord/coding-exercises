from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        orig = Counter(s1)
        length = len(s1)
        perm = Counter(s2[:length])
        if orig == perm:
            return True
        point1 = 0
        point2 = length
        while point2 < len(s2):
            old_char = s2[point1]
            new_char = s2[point2]
            perm[old_char] -= 1
            if perm[old_char] <= 0:
                del perm[old_char]
            perm[new_char] += 1
            print(perm)
            if orig == perm:
                return True
            point1 += 1
            point2 += 1
        return False