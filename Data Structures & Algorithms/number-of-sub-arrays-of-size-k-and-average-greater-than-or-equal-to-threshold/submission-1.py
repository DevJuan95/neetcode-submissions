class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        total_sum = 0
        count = 0
        target = k * threshold

        for i in range(k):
            total_sum += arr[i]
        
        if total_sum >= target:
            count += 1

        for i in range(k, n):
            total_sum += arr[i]
            total_sum -= arr[i - k]
            if total_sum >= target:
                count += 1
        return count