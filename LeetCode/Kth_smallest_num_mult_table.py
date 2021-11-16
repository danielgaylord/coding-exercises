# import heapq

# class Solution(object):
#     def findKthNumber(self, m, n, k):
#         """
#         :type m: int
#         :type n: int
#         :type k: int
#         :rtype: int
#         """
#         heap = []
#         for s in range(2, m + n + 1):
#             for x in range(1, s):
#                 y = s - x
#                 if x <= m and y <= n:
#                     heapq.heappush(heap, x * y)
#                 if len(heap) > k and s - 1 > min(m, n):
#                     break
#         return heapq.nsmallest(k, heap)[-1]

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(x):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x//i, n)
            return cnt
        
        left, right = 1, m * n
        mid = (left + right) // 2
        answer = m * n
        while left <= right:
            mid = (left + right) // 2
            ct = count(mid)
            if ct >= k:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer
