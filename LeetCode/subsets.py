class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        elems = len(nums)
        size = 2 ** elems
        results = []
        
        for item in range(size):
            unique = []
            for elem in range(elems):
                if (item >> elem) & 1:
                    unique.append(nums[elem])
            results.append(unique)
        return results