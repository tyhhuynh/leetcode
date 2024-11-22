class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minBuy = prices[0]

        for p in prices:
            maxProfit = max(maxProfit, p - minBuy)
            minBuy = min(minBuy, p)
        return maxProfit

            
                
                