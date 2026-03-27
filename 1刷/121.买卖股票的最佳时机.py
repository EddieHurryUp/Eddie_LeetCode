#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        max_profit = 0

        for p in prices:
            max_profit = max(max_profit, p-min_price)
            min_price = min(min_price, p)
        return max_profit
        

            
        
# @lc code=end

# 题目解题思路总结（121.买卖股票的最佳时机）：
# 1) 题目本质：
#    只能交易一次（买一次、卖一次），求最大利润。
#    等价于：对每个卖出日，找它之前最低的买入价。
#
# 2) 核心思路（一次遍历）：
#    - min_price：遍历到当前为止的最低价格（历史最低买入价）
#    - max_profit：遍历到当前为止的最大利润
#    每天价格 p 到来时，尝试“今天卖出”：
#    profit = p - min_price，然后更新 max_profit。
#    同时用 p 更新 min_price。
#
# 3) 为什么能从 O(n^2) 优化到 O(n)：
#    暴力法会枚举所有买卖组合；
#    优化点是把“之前最低买入价”作为状态实时维护，避免重复遍历。
#
# 4) 复杂度：
#    时间 O(n)，空间 O(1)。
#
# 5) 易错点：
#    - 忘记限制为“只能买卖一次”。
#    - 把返回值写成当天利润，而不是历史最大利润。
#    - 价格持续下降时，答案应为 0（不交易）。
