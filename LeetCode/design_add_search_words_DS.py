class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if not char in node:
                node[char] = {}
            node = node[char]
        node['$'] = True

    def search(self, word: str) -> bool:
        def search_from_node(word, node):
            for index, char in enumerate(word):
                if not char in node:
                    if char == '.':
                        for opt in node:
                            if opt != '$' and search_from_node(word[index + 1:], node[opt]):
                                return True
                    return False
                else:
                    node = node[char]
            return '$' in node
        return search_from_node(word, self.trie)
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)