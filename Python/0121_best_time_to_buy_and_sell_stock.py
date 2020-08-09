class Solution:
    def maxProfit(self, prices):
        # Set minPrice as the infininty number first to find lower value.
        minPrice = float("inf")
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit    

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))
    