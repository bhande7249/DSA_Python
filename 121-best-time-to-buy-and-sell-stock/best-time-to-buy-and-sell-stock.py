class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0;
        buy=float('inf');
        for num in prices:
            buy=min(buy,num);
            sell=num-buy;
            profit=max(sell,profit);
        return profit;