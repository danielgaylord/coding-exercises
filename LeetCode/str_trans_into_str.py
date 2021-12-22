class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        conv = {}
        uniq = set()
        for i in range(len(str1)):
            if str1[i] not in conv:
                conv[str1[i]] = str2[i]
                uniq.add(str2[i])
            else:
                if conv[str1[i]] == str2[i]:
                    continue
                else:
                    return False
        if len(uniq) < 26 or str1 == str2:
            return True
        else:
            return False