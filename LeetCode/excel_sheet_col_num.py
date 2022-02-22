class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0
        
        for index, letter in enumerate(columnTitle):
            column *= 26
            column += ord(letter) - ord("@")
        
        return column