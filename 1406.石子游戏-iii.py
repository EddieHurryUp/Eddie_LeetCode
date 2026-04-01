#
# @lc app=leetcode.cn id=1406 lang=python3
#
# [1406] 石子游戏 III
#

# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-(10**18) for _ in range(n + 1)]
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            take = 0
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    dp[i] = max(dp[i], take - dp[i + k + 1])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
                

        
# @lc code=end

# -------------------- 1406 思考过程与经验 --------------------
# 1) 核心建模：
#    定义 dp[i] 为“从下标 i 开始，当前玩家相对对手最多能领先多少分（分差）”。
#
# 2) 为什么是减号：
#    当前玩家若拿了前 k 堆得到 take，下一步轮到对手。
#    dp[i+k+1] 表示“对手在后续局面能领先的分差”，站在当前玩家视角要扣掉，
#    所以候选值是 take - dp[i+k+1]。
#
# 3) 转移方程：
#    dp[i] = max(
#        stoneValue[i] - dp[i+1],
#        stoneValue[i] + stoneValue[i+1] - dp[i+2],
#        stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]
#    )  (越界项跳过)
#
# 4) 计算顺序：
#    由于依赖 i+1 / i+2 / i+3，必须从后往前倒推（i = n-1 -> 0）。
#    边界 dp[n] = 0 表示“没有石子可拿，分差为 0”。
#
# 5) 判定结果：
#    dp[0] > 0  => Alice
#    dp[0] < 0  => Bob
#    dp[0] = 0  => Tie
#
# 6) 易错点经验：
#    - dp 要开 n+1，保证能访问 dp[n]；
#    - 初值不要用 -1000，使用极小值更稳；
#    - 尽量不要在循环中反复 sum(slice)，用 take 累加更高效。
