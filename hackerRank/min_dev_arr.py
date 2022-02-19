import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        length = len(nums)
        poss = []
        
        for index, num in enumerate(nums):
            if num % 2 == 0:
                temp = num
                poss.append((temp, index))
                while temp % 2 == 0:
                    temp //=2
                    poss.append((temp, index))
            else:
                poss.append((num, index))
                poss.append((num * 2, index))
        
        poss.sort()
        
        min_dev = inf
        need_inc = {index: 1 for index in range(length)}
        not_inc = length
        curr = 0
        
        for curr_val, curr_index in poss:
            need_inc[curr_index] -= 1
            if need_inc[curr_index] == 0:
                not_inc -= 1
            if not_inc == 0:
                while need_inc[poss[curr][1]] < 0:
                    need_inc[poss[curr][1]] += 1
                    curr += 1
                if min_dev > curr_val - poss[curr][0]:
                    min_dev = curr_val - poss[curr][0]
                
                need_inc[poss[curr][1]] += 1
                curr += 1
                not_inc += 1
        
        return min_dev