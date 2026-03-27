#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

#%%
# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "]":"[", "}":"{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1]!= pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)   
        return not stack
        
# @lc code=end
sol = Solution()
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))  # False



# 栈知识点（Python）：
# 1) 常用容器：list 即可作为栈（后进先出，LIFO）。
# 2) 基本操作：
#    - 入栈：stack.append(x)
#    - 取栈顶：stack[-1]
#    - 出栈：stack.pop()
#    - 判空：if not stack
# 3) 使用习惯：
#    pop() / stack[-1] 前先判空，避免越界错误。
#
# 本题知识点（20.有效的括号）：
# 1) 题目本质：
#    括号匹配问题，满足“后开先关” -> 典型栈模型。
# 2) 核心思路：
#    - 左括号：入栈
#    - 右括号：检查栈顶是否为对应左括号
#      若栈空或不匹配，直接 False；匹配则 pop。
# 3) 关键技巧：
#    使用映射 pairs = {')':'(', ']':'[', '}':'{'}，O(1) 判断匹配关系。
# 4) 收尾判断：
#    遍历完成后 return not stack；栈非空说明仍有未闭合左括号。
# 5) 复杂度：
#    时间 O(n)，空间 O(n)。
# 6) 易错点：
#    - 忘记处理“右括号时栈为空”。
#    - 只统计数量，不校验顺序（顺序错误也应判 False）。
