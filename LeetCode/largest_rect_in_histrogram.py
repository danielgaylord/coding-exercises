class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for index, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= height:
                curr_height = heights[stack.pop()]
                curr_width = index - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(index)
        
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, curr_height * curr_width)
        
        return max_area