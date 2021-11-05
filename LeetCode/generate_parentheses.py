class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def dfs(string, open, close):
            if open == 0 and close == 0:
                result.append(string)
            if open > 0:
                dfs(string + "(", open - 1, close + 1)
            if close > 0:
                dfs(string + ")", open, close - 1)
        dfs("", n, 0)
        return result