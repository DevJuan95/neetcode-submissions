class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = prices[0]

        for i in range(1, len(prices)):
            if current_min > prices[i]:
                current_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - current_min)
        
        return max_profit
        