#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for L in range(2, n+1):
            for i in range(0, n-L+1):
                j = i + L - 1 # 小于n
                take_left = nums[i] - dp[i+1][j]
                take_right = nums[j] - dp[i][j-1]
                dp[i][j] = max(take_left, take_right)
        
        return dp[0][n-1] >=0

        
# @lc code=end

# -------------------- 思考思路总结 --------------------
# 1) 把“先手能不能赢”改写成“当前玩家相对对手最多能领先多少分”。
#    定义 dp[i][j]：在区间 nums[i..j] 中，当前玩家相对对手的最大分差。
#
# 2) 基础情况：
#    只剩一个数时，当前玩家只能拿它，所以 dp[i][i] = nums[i]。
#
# 3) 状态转移（当前玩家二选一）：
#    - 选左端 nums[i]：得到 nums[i]，随后对手在 [i+1..j] 能领先 dp[i+1][j]，
#      因此当前玩家净领先 = nums[i] - dp[i+1][j]。
#    - 选右端 nums[j]：净领先 = nums[j] - dp[i][j-1]。
#    取更优：dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])。
#
# 4) 为什么按区间长度循环：
#    dp[i][j] 依赖更短区间 dp[i+1][j]、dp[i][j-1]，
#    所以先算长度 1，再算长度 2...直到 n（典型倒推区间 DP）。
#
# 5) 最终答案：
#    若 dp[0][n-1] >= 0，表示先手至少不输（可赢或平），返回 True；
#    否则返回 False。
