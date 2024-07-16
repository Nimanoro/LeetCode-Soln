class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, mx = 0, 1, 0
        while right < len(prices):
            if prices[right] > prices[left]:
                mx = max(mx, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
        return mx