#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

from collections import Counter
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        cnt = Counter()
        for right in range(len(s)):
            cnt[s[right]] += 1
            while cnt[s[right]] > 1:
                cnt[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
            

        
# @lc code=end

if __name__ == "__main__":
    s = input().rstrip("\n")
    print(Solution().lengthOfLongestSubstring(s))

# 题目知识点总结（3.无重复字符的最长子串）：
# 1) 核心模型：滑动窗口 + 计数哈希（Counter）
#    - 用 [left, right] 表示当前窗口，窗口内始终保持“无重复字符”。
#    - right 右移扩窗；若新字符重复，则 left 右移缩窗直到恢复无重复。
#
# 2) 关键不变量：
#    - while 循环结束后，窗口内每个字符出现次数都 <= 1。
#    - 每一轮都可用 right - left + 1 更新“当前合法窗口长度”。
#
# 3) 时间复杂度：
#    - O(n)，n 为字符串长度。
#    - right 从左到右遍历一次；left 也只会单调右移，最多移动 n 次。
#
# 4) 空间复杂度：
#    - O(k)，k 为字符集大小（最坏 O(n)）。
#    - 额外空间来自 Counter 记录窗口内字符计数。
#
# 5) Counter 知识点（collections.Counter）：
#    - 本质：dict 的子类，用于“元素 -> 计数”。
#    - 常见操作：
#      cnt[ch] += 1    # 元素计数 +1（不存在时默认从 0 开始）
#      cnt[ch] -= 1    # 元素计数 -1
#      cnt[ch]         # 读取计数，不存在返回 0
#    - 在滑动窗口中的作用：
#      O(1) 维护窗口内字符频次，快速判断是否出现重复（cnt[ch] > 1）。
