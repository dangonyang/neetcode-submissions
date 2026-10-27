class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        # base case (so ways to get 0 dollars)
        dp[0] = 0

        # need to iterate through each amount and check their ways
        for hit in range(1, amount + 1):
            # go through all coins
            for c in range(len(coins)):
                # if current coin doesn't exceed target
                if coins[c] <= hit:
                    # set target to minimum of target (using previous problem or current target)
                    dp[hit] = min(dp[hit], dp[hit - coins[c]] + 1)
        # return the amount
        return dp[amount] if dp[amount] != float('inf') else -1