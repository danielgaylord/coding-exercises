class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * k for k in range(1, 102)]
        glasses[0][0] = poured
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                pour = (glasses[row][col] - 1.0) / 2.0
                if pour > 0:
                    glasses[row + 1][col] += pour
                    glasses[row + 1][col + 1] += pour
        
        return min(1, glasses[query_row][query_glass])