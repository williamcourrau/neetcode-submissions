class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):

            buy = prices[left] # 7
            sell = prices[right] # 1

            if buy >= sell:
                left = right
            elif buy < sell:
                max_profit = max(max_profit, sell - buy)
            
            right += 1 
        
        return max_profit

