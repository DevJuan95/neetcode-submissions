class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n,i):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            return dfs(n-1, i) + dfs(n-2, i)
        
        return dfs(n,0)
        