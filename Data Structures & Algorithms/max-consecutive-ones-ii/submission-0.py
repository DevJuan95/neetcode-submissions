class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_count = 0
        window_zc = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                window_zc += 1
            if window_zc < 2:
                max_count = max(max_count, (r - l) + 1)
            else:
                l = r - 1
                window_zc -= 1
        return max_count