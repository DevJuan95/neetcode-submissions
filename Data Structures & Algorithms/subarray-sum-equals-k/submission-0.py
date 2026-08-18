class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixCount = {0:1}

        for num in nums:
            curSum += num
            j = curSum - k

            res += prefixCount.get(j,0)
            prefixCount[curSum] = 1 + prefixCount.get(curSum,0)
        
        return res
