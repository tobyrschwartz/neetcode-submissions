class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        left, right = 0, 1
        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
        return max_profit