class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for loc in path.split("/"):
            if loc == "..":
                if stack:
                    stack.pop()
            elif loc == "." or not loc:
                continue
            else:
                stack.append(loc)
        
        return "/" + "/".join(stack)