class Node:
    def __init__(self):
        self.isWord = False
        self.children = [0] * 26
        
class Trie:
    def __init__(self):
        root = Node()
        self.trie = list([root])
        
    def add(self, word):
        cur = 0
        for char in word:
            i = ord(char) - ord('a')
            if not self.trie[cur].children[i]:
                root = Node()
                self.trie[cur].children[i] = len(self.trie)
                self.trie.append(root)
            cur = self.trie[cur].children[i]
        self.trie[cur].isWord = True
                
    def hasSuffix(self, stream):
        cur = 0
        for char in stream:
            i = ord(char) - ord('a')
            if not self.trie[cur].children[i]:
                return False
            cur = self.trie[cur].children[i]
            if self.trie[cur].isWord:
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])
        self.stream = ""

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        return self.trie.hasSuffix(self.stream)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)