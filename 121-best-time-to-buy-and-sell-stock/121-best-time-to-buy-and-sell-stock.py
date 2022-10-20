class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices[i] = num
        return max(maxProfit, otherNum))
        use Two pointer
        if cannot achieve any profit return 0
        [7,1,5,3,6,4]
        lp rp
        rp = sell
        lp is buy
        while rp < len(prices):
            prices[right] - prices[left]:
                max_profit = max(currentProfit, maxProfit)
                #keep a maxProfit counter outside the while loop
        """
        
        l, r = 0, 1
        maxProfit = 0
        
        while r < len(prices):
            currentProfit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxProfit = max(currentProfit, maxProfit)
            else:
                l = r 
            r += 1
        return maxProfit
    
    