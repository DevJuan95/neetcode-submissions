class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)

        extra = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        max_extra = extra

        for i in range(minutes,n):
            if grumpy[i] == 1:
                extra += customers[i]
            
            left = i - minutes
            if grumpy[left] == 1:
                extra -= customers[left]
            max_extra = max(extra, max_extra)
        
        return base + max_extra