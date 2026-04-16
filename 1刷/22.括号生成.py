#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(path, left, right):
            if len(path) == 2 * n:
                ans.append(path)
                return
            
            if left < n:
                dfs(path + "(", left + 1, right)
            
            if right < left:
                dfs(path + ")", left, right + 1)

        dfs("", 0, 0)
        return ans


# @lc code=end

# 解题思路（回溯 + 剪枝）：
# 1) 把问题看成在每一步选择放 "(" 或 ")" 的决策树搜索。
# 2) 状态定义：
#    - path: 当前已构造的括号字符串
#    - left: 已使用的左括号数量
#    - right: 已使用的右括号数量
# 3) 终止条件：
#    - 当 len(path) == 2 * n，说明构造完成，加入答案。
# 4) 剪枝条件（合法性约束）：
#    - 只有 left < n 才能继续放 "("
#    - 只有 right < left 才能继续放 ")"（保证任意前缀都合法）
#
# 复杂度：
# - 时间复杂度约为 O(Cn * n)，Cn 为第 n 个卡特兰数（需要生成全部合法解，每个解长度为 2n）
# - 空间复杂度 O(n)（递归栈深度）
