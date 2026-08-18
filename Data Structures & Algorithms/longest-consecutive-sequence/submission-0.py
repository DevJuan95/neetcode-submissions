class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapa = {}
        for num in nums:
            mapa[num] = num

        longest = 0
        for i in range(len(nums)):
            num = nums[i]
            current_longest = 0
            if (num - 1 ) not in mapa:
                while num in mapa:
                    current_longest +=1
                    num +=1
            if current_longest >= longest:
                longest = current_longest
        return longest