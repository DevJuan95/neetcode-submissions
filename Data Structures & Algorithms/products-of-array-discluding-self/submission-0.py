class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num !=0:
                product = product * num
            else:
                zero_count +=1
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                if num !=0:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // num
        return res

        
            