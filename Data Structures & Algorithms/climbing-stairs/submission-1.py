class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(r):
            if r >= n:
                if n == r:
                    return 1;
                else:
                    return 0;
            return dfs(r+1) + dfs(r+2)

        return dfs(0)
        