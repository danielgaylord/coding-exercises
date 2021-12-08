from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            keyList = self.timeMap[key]
            if timestamp < keyList[0][0]:
                return ""
            if timestamp > keyList[-1][0]:
                return keyList[-1][1]
            left, right = 0, len(keyList) - 1
            while left <= right:
                mid = (left + right) // 2
                keyStamp = keyList[mid][0]
                if keyStamp == timestamp:
                    return keyList[mid][1]
                elif keyStamp < timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
            return keyList[right][1]
                
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)