class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        greatest = -1
        for i in range(n-1 , - 1, -1):
            res[i] = greatest
            if arr[i] > greatest:
                greatest = arr[i]

        return res