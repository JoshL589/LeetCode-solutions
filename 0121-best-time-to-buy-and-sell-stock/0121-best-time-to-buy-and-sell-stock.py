class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit is buying for cheap and selling it a different day, l is buying r is selling, you should only update l if you can buy a cheaper one and you keep checking how much profit you can make by checking the difference between l and r
        l = 0
        r = 0
        max_profit = 0
        while r < len(prices):
            print(max_profit)
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return max_profit