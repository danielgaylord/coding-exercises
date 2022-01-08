class File:
    def __init__(self):
        self.isfile = False
        self.files = {}
        self.content = ""

class FileSystem:
    
    def __init__(self):
        self.root = File()

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(list(self.root.files.keys()))
        
        path = path.split("/")
        loc = self.root
        for dir in path[1:]:
            loc = loc.files[dir]
            if loc.isfile:
                return [dir]
        
        return sorted(list(loc.files.keys()))
            

    def mkdir(self, path: str) -> None:
        path = path.split("/")
        loc = self.root
        for dir in path[1:]:
            if dir not in loc.files:
                loc.files[dir] = File()
            loc = loc.files[dir]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")
        loc = self.root
        for dir in path[1:]:
            if dir not in loc.files:
                loc.files[dir] = File()
            loc = loc.files[dir]
        loc.content += content
        loc.isfile = True

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")
        loc = self.root
        for dir in path[1:]:
            loc = loc.files[dir]
        
        return loc.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)