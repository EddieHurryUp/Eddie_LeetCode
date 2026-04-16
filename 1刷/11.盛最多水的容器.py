#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# @lc code=end

# 解题思路（双指针 + 贪心）：
# 1) 用 left/right 分别指向数组两端，当前面积为 min(height[left], height[right]) * (right-left)。
# 2) 每次只移动较短的那一边：
#    - 因为宽度一定会变小；
#    - 若移动较高的一边，短板不变，面积不可能变大；
#    - 只有移动短板，才可能遇到更高柱子，让短板抬高，产生更大面积。
# 3) 过程中持续更新最大面积，直到 left >= right。
#
# 复杂度：
# - 时间 O(n)：每个指针最多移动 n 次
# - 空间 O(1)：只使用常数额外变量
