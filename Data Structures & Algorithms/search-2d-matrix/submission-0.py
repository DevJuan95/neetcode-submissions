class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search starts at 0,0 and m,n
        #calculate the mid point
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1
        COLS = len(matrix[0])




        
        while left <= right:
            mid = (left + right) // 2
            row = mid // COLS
            col = mid % COLS
            val = matrix[row][col]
            if val > target:
                right = mid - 1
            elif val < target:
                left = mid + 1
            else:
                return True
        return False