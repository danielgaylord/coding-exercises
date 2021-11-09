"""
class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """"""
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """"""
        result = []
        wordhash = {}
        for puzzle in puzzles:
            count = 0
            puzzleset = set(puzzle)
            for word in words:
                if word in wordhash:
                    wordset = wordhash[word]
                else:
                    wordset = set(word)
                if puzzle[0] in word and len(wordset.difference(puzzleset)) == 0:
                    count += 1
            result.append(count)
        return result
"""

class Solution(object):
    def bitMask(self, word):
        mask = 0
        for char in word:
            i = ord(char) - ord('a')
            mask |= 1 << i
        return mask
    
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        freq = {}
        result = [0 for _ in range(len(puzzles))]
        for word in words:
            mask = self.bitMask(word)
            freq[mask] = freq.get(mask, 0) + 1
        for index, puzzle in enumerate(puzzles):
            mask = self.bitMask(puzzle)
            submask = mask
            total = 0
            firstbitdex = ord(puzzle[0]) - ord('a')
            while True:
                if submask >> firstbitdex & 1:
                    total += freq.get(submask, 0)
                if submask == 0:
                    break
                submask = (submask - 1) & mask
            result[index] = total
        return result
