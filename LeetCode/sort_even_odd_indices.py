class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        
        if len(nums) <= 2:
            return nums
        
        for index, val in enumerate(nums):
            if index % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        
        even.sort()
        odd.sort(reverse=True)
        
        for index in range(len(nums)):
            if index % 2 == 0:
                nums[index] = even[index // 2]
            else:
                nums[index] = odd[(index // 2)]
        
        print(nums)
        return nums