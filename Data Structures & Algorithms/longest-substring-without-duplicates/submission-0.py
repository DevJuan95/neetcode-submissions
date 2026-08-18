class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 0
        n = len(s)
        if n < 1:
            return 0
        for i in range(n):
            seen = {}
            seen.update({s[i]: s[i]})
            counter = 1
            for j in range(i+1, n):
                if s[j] not in seen:
                    seen.update({s[j]: s[j]})
                    counter += 1
                else:
                    break
            
            max_lenght = max(max_lenght, counter)
        
        return max_lenght