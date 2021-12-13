class Solution:
    def maxPower(self, s: str) -> int:
        power = 1
        temp = 1
        for idx in range(1, len(s)):
            if s[idx] == s[idx - 1]:
                temp += 1
            else:
                temp = 1
            power = max(power, temp)
        return power