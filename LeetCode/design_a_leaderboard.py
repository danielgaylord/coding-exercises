import heapq
from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        top = self.scores.values()
        heapq.heapify(list(top))
        return sum(heapq.nlargest(K, top))

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)