class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i=0
        buy=float('inf')
        sell=0
        profit=0
        while i<len(prices):
            buy=min(buy,prices[i])
            sell=prices[i]
            curProfit=sell-buy
            profit=max(curProfit,profit)
            i+=1
        return profit