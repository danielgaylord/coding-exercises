class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_diff = float('inf')
        for index in range(1, len(arr)):
            local_diff = abs(arr[index] - arr[index - 1])
            if local_diff < min_diff:
                min_diff = local_diff
                result = []
                result.append([arr[index - 1], arr[index]])
            elif local_diff == min_diff:
                result.append([arr[index - 1], arr[index]])
        return result