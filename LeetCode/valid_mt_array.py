class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        increase = True
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            elif i == 1 and arr[i] < arr[i - 1]:
                return False
            elif increase and arr[i] < arr[i - 1]:
                increase = False
            elif not increase and arr[i] > arr[i - 1]:
                return False
        
        return not increase