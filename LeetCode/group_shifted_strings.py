from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        bases = defaultdict(list)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        for string in strings:
            diff = ord(string[0]) - ord('a')
            check = ""
            for char in string:
                new_ord = ord(char) - diff #need to mod for alpha
                if new_ord < 97:
                    new_ord = 123 - (97 - new_ord)
                check += chr(new_ord)
            print(check)
            bases[check].append(string)
        
        result = []
        for key, value in bases.items():
            result.append(value)
        return result
                