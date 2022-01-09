class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        face = 0
        start = (0,0)
        poss = set(start)
        loc = start
        for instruction in instructions:
            if instruction == "G":
                loc = (loc[0] + dirs[face][0], loc[1] + dirs[face][1])
                poss.add(loc)
            elif instruction == "L":
                face -= 1
                if face == -1:
                    face = 3
            elif instruction == "R":
                face += 1
                if face == 4:
                    face = 0
        if loc == start:
            return True
        if face != 0:
            return True
        return False
        
        