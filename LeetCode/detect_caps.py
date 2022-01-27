class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allCaps = True
        allLower = True
        
        for char in word[1:]:
            allCaps = allCaps and char.isupper()
            allLower = allLower and char.islower()
        
        if (allCaps and word[0].isupper()) or (allLower and word[0].islower()) or (allLower and word[0].isupper()):
            return True

        return False
        
# Simpler
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())                