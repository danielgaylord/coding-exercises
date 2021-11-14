class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combos = []
        for b in range(1 << len(characters)):
            if bin(b).count('1') == combinationLength:
                hold = ""
                for index in range(len(characters)):
                    if (b & (1 << index)) > 0:
                        hold += characters[index]
                self.combos.append(hold)
        self.combos.sort(reverse=True)

    def next(self) -> str:
        if self.combos:
            return self.combos.pop()
        else:
            return None

    def hasNext(self) -> bool:
        if self.combos:
            return True
        else:
            return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()