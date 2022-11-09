from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        if len(prices) < 2:
            return profit
        buy = (prices[0], 0)
        sell = (prices[1], 1)
        for i in range(1, len(prices)):
            if prices[i] < buy[0]:
                buy = (prices[i], i)
            else:
                sell = (prices[i], i)

            profit = max(profit, sell[0] - buy[0] if buy[1] < sell[1] else 0)

        return profit

    def maxProfitSimple(self, prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[
                left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

        # Wrong TA Limit O(n**2)
        # for i in range(len(prices) - 1):
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])


sol = Solution()
prices = [7,1,5,3,6,4]
assert sol.maxProfit(prices=prices) == 5
prices = [7,6,4,3,1]
assert sol.maxProfit(prices=prices) == 0
prices = [7]
assert sol.maxProfit(prices=prices) == 0
