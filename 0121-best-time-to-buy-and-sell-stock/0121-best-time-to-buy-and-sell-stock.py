class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        ans = 0
        
        while r <len(prices):
            if prices[r] < prices[l]:
                l = r
            cur = prices[r] - prices[l]
            r += 1
            ans = max(ans, cur)
            
        return ans