class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {char: index for index, char in enumerate(s)}
        curr = start = 0
        result = []
        
        for index, char in enumerate(s):
            curr = max(curr, last_occurence[char])
            if index == curr:
                result.append(index - start + 1)
                start = index + 1
        
        return result