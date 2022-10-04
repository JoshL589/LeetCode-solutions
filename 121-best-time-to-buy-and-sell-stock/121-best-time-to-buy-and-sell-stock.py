class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            cur_profit = prices[r] - prices[l]
            if max_profit < cur_profit:
                max_profit = cur_profit
            if prices[l] > prices[r]:
                l = r
            r += 1
        return max_profit