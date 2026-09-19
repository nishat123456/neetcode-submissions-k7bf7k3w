class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #r goes all the way, l from 0
        #if profit, update max profit.
        #if find lower price, move l to r, shesh
        l = 0
        profit = 0
        maxP = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                print(profit)

            else:
                l = r

        return maxP 
