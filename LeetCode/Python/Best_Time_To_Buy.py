class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = buying_and_selling(prices)
        return profit
    
def buying_and_selling(input_prices):
    profit = 0
    buying_price = input_prices[0]
    for i in range(1,len(input_prices)):
        if(input_prices[i]>buying_price):
            profit = max(profit,input_prices[i]-buying_price)
        elif(input_prices[i]<buying_price):
            buying_price = input_prices[i]
        else:
            pass
    return profit
