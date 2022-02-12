from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        length = len(beginWord)
        poss_dict = defaultdict(list)
        for word in wordList:
            for index in range(length):
                poss_dict[word[:index] + "*" + word[index + 1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            currentWord, pathSize = queue.popleft()
            for index in range(length):
                possWord = currentWord[:index] + "*" + currentWord[index + 1:]
                for word in poss_dict[possWord]:
                    if word == endWord:
                        return pathSize + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, pathSize + 1))
                poss_dict[possWord] = []
        return 0