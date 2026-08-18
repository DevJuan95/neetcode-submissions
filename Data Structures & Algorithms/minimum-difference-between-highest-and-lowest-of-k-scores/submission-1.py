class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = nums[n-1]

        for i in range(0, n - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])
        return min_diff