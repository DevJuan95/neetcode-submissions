class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            l = i 
            r = (len(s) - 1) - i
            aux = s[r]
            s[r] = s[l]
            s[l] = aux
        
        