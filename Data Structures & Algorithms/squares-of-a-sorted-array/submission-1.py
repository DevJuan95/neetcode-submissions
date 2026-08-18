class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #two pointers if nums[l] > nums[r]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        p = len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                #swap and move l
                res[p] = pow(nums[l], 2)
                l+=1

            else:
                res[p] = pow(nums[r], 2)
                r -= 1
            p -= 1
        return res