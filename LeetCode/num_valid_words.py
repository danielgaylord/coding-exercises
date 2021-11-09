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
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """