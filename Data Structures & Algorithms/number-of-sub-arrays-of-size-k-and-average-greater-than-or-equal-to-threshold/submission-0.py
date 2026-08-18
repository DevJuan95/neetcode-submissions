class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total_count = 0
        n = len(arr)
        for i in range(n - k + 1):
            total = 0
            for j in range(i, i + k):
                total += arr[j]
            if total / k >= threshold:
                total_count += 1
        return total_count