class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        palindromes = set()
        
        def palindHelper(res, curr, string):
            if len(string) == 0:
                res.append(curr)
                return
            
            for i in range(1, len(string) + 1):
                piece = string[:i]
                if piece in palindromes or piece == piece[::-1]:
                    palindromes.add(piece)
                    palindHelper(res, curr + [piece], string[i:])
        
        palindHelper(results, [], s)
        return results
                    