class Solution:
    def trap(self, height: List[int]) -> int:
        ##calculate the prefix and suffix
        n = len(height)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = max(prefix[i], height[i])
        
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        print(prefix)
        print(suffix)
        total_area = 0
        for i in range(n):
            area = min(prefix[i+1], suffix[i]) - height[i]
            if area > 0:
                total_area += area

        return total_area
