class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorList = {}
        for color in nums:
            if color not in colorList:
                colorList[color] = 1
            else:
                colorList[color] += 1
        
        index = 0
        for color in sorted(colorList):
            for _ in range(colorList[color]):
                nums[index] = color
                index += 1