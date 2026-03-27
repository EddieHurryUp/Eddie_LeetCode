#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            ans = max(ans, dp[i])
        return ans
        
# @lc code=end

# 题目知识点总结（53.最大子数组和）：
# 1) 题目本质：
#    在“连续子数组”里找和最大的那一段。
#    关键是“连续”，所以当前位置只和前一位置状态相关。
#
# 2) 动态规划定义：
#    dp[i] 表示“必须以 nums[i] 结尾”的最大子数组和。
#
# 3) 状态转移：
#    dp[i] = max(nums[i], dp[i-1] + nums[i])
#    含义：当前位置要么单独开新段，要么接在前一段后面。
#
# 4) 答案维护：
#    全局答案 ans = max(ans, dp[i])。
#
# 5) 复杂度：
#    时间 O(n)，空间 O(n)（dp 数组写法）。
#    可优化到 O(1)：只保留“上一状态 cur”和“全局最优 best”。
#
# 6) 易错点：
#    - 把题目当成“任意子序列”而不是“连续子数组”。
#    - 全负数场景处理错误（初始化应以 nums[0] 开始）。
#    - 忘记每轮更新全局最大值 ans。
