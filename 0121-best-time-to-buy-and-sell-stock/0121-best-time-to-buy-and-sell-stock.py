class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if min_price > price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit