class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        #check the current, then check if current is equal to the others terms sum with subrange.
        for i in range(0, len(prefix)):
            rest = prefix[len(prefix) - 1] - (prefix[i-1] if i > 0 else 0)
            if prefix[i] == rest:
                return i
        
        return -1