class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        while len(v1) < len(v2):
            v1.append("0")
        while len(v2) < len(v1):
            v2.append("0")
            
        for index, revs in enumerate(list(zip(v1, v2))):
            rev1, rev2 = revs
            if int(rev1) < int(rev2):
                return -1
            elif int(rev1) > int(rev2):
                return 1
        
        return 0