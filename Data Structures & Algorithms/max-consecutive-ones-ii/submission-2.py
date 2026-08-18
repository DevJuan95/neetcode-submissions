class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_secuence = 0
        for l in range(len(nums)):
            zeros_count = 0
            for r in range(l, len(nums)):
                if nums[r] == 0:
                    zeros_count +=1
                if zeros_count == 2:
                    break;
                
                longest_secuence = max(longest_secuence, r - l + 1)
        return longest_secuence