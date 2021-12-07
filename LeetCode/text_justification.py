from collections import deque

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        queue = deque(words)
        result = []
        
        while queue:
            chars = 0
            temp = []
            lastLine = False
            while chars + len(queue[0]) + len(temp) <= maxWidth:
                chars += len(queue[0])
                temp.append(queue.popleft())
                if len(queue) == 0:
                    lastLine = True
                    break
            spaces = maxWidth - chars
            if lastLine:
                space_per = 1 
            elif len(temp) > 1:
                space_per = spaces // (len(temp) - 1)
            else:
                space_per = 0
            extra_spaces = spaces - (space_per * (len(temp) - 1))
            line = ""
            for i in range(len(temp)):
                line += temp[i]
                if i < len(temp) - 1:
                    line += " " * space_per
                if not lastLine and len(temp) > 1 and extra_spaces > 0:
                    line += " "
                    extra_spaces -= 1
            line += " " * extra_spaces
                        
            result.append(line)
        return result