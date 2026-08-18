class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            l = i
            r = i + 1
            height = heights[i]
            while l >= 0 and heights[l] >= height: 
                #calculate the area
                l-=1
            while r < len(heights) and heights[r] >= height:
                r+=1
            
            r-=1
            l+=1
            width = (r - l + 1)
            max_area = max(max_area, self.calculateArea(height, width))
        return max_area
            
    
    def calculateArea(self, height: int, width: int):
        return height * width