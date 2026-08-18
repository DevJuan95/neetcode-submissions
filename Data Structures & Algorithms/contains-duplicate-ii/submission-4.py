class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} # value : index
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                r = abs( seen[nums[i]] -  i)
                if r <= k:
                    return True
                seen[nums[i]] = i
        return False