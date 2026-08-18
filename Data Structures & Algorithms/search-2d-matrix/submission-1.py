class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array_1d = [element for sublist in matrix for element in sublist]
        return target in set(array_1d)