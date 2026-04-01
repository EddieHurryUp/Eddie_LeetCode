#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 由于石子总数为奇数，所以玩家1和玩家2不可能平局。
        # 玩家1和玩家2都采用最佳策略，玩家1总是能够获得更多的石子，因此玩家1获胜。
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for L in range(2, n+1):
            for i in range(0, n-L+1):
                j = i + L - 1
                take_left = piles[i] - dp[i+1][j]
                take_right = piles[j] - dp[i][j-1]
                dp[i][j] = max(take_left, take_right)
        return dp[0][n-1] > 0
        
# @lc code=end

