class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create dp 2d array
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # for each row starting at last char in text1
        for r in range(len(text1) - 1, -1, -1):
            # for each col starting at last char in text2
            for c in range(len(text2) - 1, -1, -1):
                # if char at text1 == char at text2
                if text1[r] == text2[c]:
                    # add 1 and go diagonal (down right)
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                # else
                else:
                    # set dp to max value between right col or up col
                    dp[r][c] = max(dp[r][c + 1], dp[r + 1][c])
        return dp[0][0]