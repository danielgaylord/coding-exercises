class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        main_max = float('-inf')
        main_min = float('inf')
        max_arr = -1
        min_arr = -1
        for i in range(len(arrays)):
            check = arrays[i]
            if check[-1] > main_max:
                main_max = check[-1]
                max_arr = i
            if check[0] < main_min:
                main_min = check[0]
                min_arr = i
        
        sub_max = float('-inf')
        sub_min = float('inf')
        for i in range(len(arrays)):
            check = arrays[i]
            if check[-1] > sub_max and i != min_arr:
                sub_max = check[-1]
            if check[0] < sub_min and i != max_arr:
                sub_min = check[0]
            
        return max(main_max - sub_min, sub_max - main_min)