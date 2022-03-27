class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = [(sum(row), index) for index, row in enumerate(mat)]
        strength.sort(key = lambda x: x[0])  
        return [index for s, index in strength[:k]]