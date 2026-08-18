class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rightmost = len(digits) - 1
        res = digits[:]
        while rightmost >= 0 and digits[rightmost] == 9:
            res[rightmost] = 0
            rightmost -=1
        if rightmost >= 0:
            res[rightmost]+=1
        else:
            res = [1] + res
        return res
