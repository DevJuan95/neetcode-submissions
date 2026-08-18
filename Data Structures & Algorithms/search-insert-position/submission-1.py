class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid
        return l