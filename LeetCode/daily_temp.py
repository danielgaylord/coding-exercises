class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numtemp = len(temperatures)
        result = [0 for _ in range(numtemp)]
        maxes = [numtemp - 1]
        for index in range(numtemp -2, -1, -1):
            while maxes and temperatures[index] >= temperatures[maxes[-1]]:
                maxes.pop()
            if len(maxes) == 0:
                result[index] = 0
            else:
                result[index] = maxes[-1] - index
            maxes.append(index)
        return result