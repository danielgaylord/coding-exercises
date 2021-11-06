from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = deque()
        mapping = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        for num in digits:
            if len(result) == 0:
                result.append("")
            for item in range(len(result)):
                prev = result.popleft()
                for letter in mapping[int(num)]:
                    result.append(prev + letter)
        return list(result)