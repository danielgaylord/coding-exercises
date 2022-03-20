class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check_match(num):
            rot_a = rot_b = 0
            for index in range(length):
                if tops[index] != num and bottoms[index] != num:
                    return -1
                elif tops[index] != num:
                    rot_a += 1
                elif bottoms[index] != num:
                    rot_b += 1
                
            return min(rot_a, rot_b)
        
        length = len(tops)
        rotations = check_match(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check_match(bottoms[0])