class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        pointerOne = 0
        pointerTwo = 1

        while pointerTwo < len(prices):
            if prices[pointerOne] >= prices[pointerTwo]:
                pointerOne = pointerTwo
                pointerTwo += 1
            else:
                localProfit = prices[pointerTwo] - prices[pointerOne]
                if profit < localProfit:
                    profit = localProfit
                pointerTwo += 1


        return profit
        