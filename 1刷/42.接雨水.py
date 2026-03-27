#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import List

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0] * len(height)
        for i, h in enumerate(height):
            if i == 0:
                l[i] = h
            else:
                l[i] = max(l[i-1], h)
        r = [0] * len(height)
        for j in range(len(height)-1, -1, -1):
            if j == len(height) -1:
                r[j] = height[j]
            else:
                r[j] = max(r[j+1], height[j])
        
        ans = 0
        for i, h in enumerate(height):
            ans += min(l[i], r[i]) - h
        return ans
        
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))  # 9

# 题目经验总结（42.接雨水）：
# 1) 核心结论：
#    每个位置 i 能接的水量只由两侧最高挡板中较矮的一侧决定：
#    water[i] = min(left_max[i], right_max[i]) - height[i]。
#
# 2) 本代码思路（前后缀最大值）：
#    - l[i] 表示 [0..i] 的最高柱子。
#    - r[i] 表示 [i..n-1] 的最高柱子。
#    - 最后遍历每个位置累加 min(l[i], r[i]) - height[i]。
#
# 3) 复杂度：
#    - 时间复杂度 O(n)：3 次线性遍历（构建 l、构建 r、求和）。
#    - 空间复杂度 O(n)：额外使用了两个长度为 n 的数组。
#
# 4) 常见易错点：
#    - 忘记是“较矮挡板”决定上限（应取 min，不是 max）。
#    - 把“柱子高度”直接相加而非“可接水高度”相加。
#    - 左右最大值数组下标或边界初始化写错。
#
# 5) 面试描述模板（可直接复述）：
#    “我先基于木桶短板原理：位置 i 的水位上限由左右最高柱中较小者决定。
#    所以先预处理每个位置左侧最高 left_max 和右侧最高 right_max，
#    然后累加 min(left_max[i], right_max[i]) - height[i]。
#    这样避免了对每个位置重复向两边搜索，把 O(n^2) 优化到 O(n)。”
#
# 6) 面试加分点（进阶优化）：
#    - 可以用双指针把空间从 O(n) 优化到 O(1)：
#      维护 left/right 与 left_max/right_max，始终移动较矮一侧并结算该侧水量。
