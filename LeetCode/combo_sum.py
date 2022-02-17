class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def helper(curr, position, remainder):
            if remainder == 0:
                results.append(list(curr))
                return
            elif remainder < 0:
                return
            
            for index in range(position, len(candidates)):
                curr.append(candidates[index])
                helper(curr, index, remainder - candidates[index])
                curr.pop()
        
        helper([], 0, target)
        
        return results