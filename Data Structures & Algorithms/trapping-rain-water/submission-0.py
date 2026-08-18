class Solution:
    def trap(self, height: List[int]) -> int:
        total_area =0
        for i in range(len(height)):
            #search for tallest in left and right
            r = i + 1
            left_tallest = 0
            right_tallest = 0
            for l in range(i - 1,-1,-1):
                left_tallest = max(height[l], left_tallest)
            for r in range(i + 1, len(height)):
                right_tallest = max(height[r], right_tallest)
            
            area = min(left_tallest, right_tallest) - height[i]
            if area > 0:
                total_area += area
        return total_area