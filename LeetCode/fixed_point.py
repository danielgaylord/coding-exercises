class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1
        curr = inf
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if arr[mid] == mid:
                curr = min(curr, mid)
            
            if arr[mid] >= mid:
                hi = mid
            else:
                lo = mid + 1
        
        if curr >= 0 and curr != inf:
            return curr
        else:
            return -1