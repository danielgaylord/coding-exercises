from collections import deque

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        result = []
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        while pos:
            result.append(pos.popleft())
            result.append(neg.popleft())
        
        return result
        