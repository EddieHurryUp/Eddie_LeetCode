#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
# 有空位+原地->从后往前
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n -1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
# @lc code=end

# ===== 题目总结与经验 =====
# 1) 思路触发条件（看到就要警觉）
# - 要求“原地修改 nums1”
# - nums1 末尾有足够空位
# - 两个数组本身有序
# => 直接触发：双指针从后往前填充。
#
# 2) 核心不变量
# - i 指向 nums1 有效区末尾，j 指向 nums2 末尾，k 指向 nums1 总末尾。
# - 每一轮都把更大的值放到 nums1[k]，然后对应指针左移。
#
# 3) 为什么必须从后往前
# - 从前往后会覆盖 nums1 里还没比较的数据，通常要做整体搬移，复杂度变差且易错。
# - 从后往前刚好利用尾部空位，不会覆盖有效数据。
#
# 4) 常见易错点
# - 忘记 while 条件写成 i >= 0 and j >= 0。
# - 误以为还要补 nums1 剩余元素：其实不用，nums1 剩下的本来就在正确位置。
# - k 左移时机写漏，导致覆盖错位。
#
# 5) 复杂度
# - 时间复杂度：O(m + n)
# - 空间复杂度：O(1)
#
# 6) 记忆口诀
# - “有空位 + 原地改 = 从后往前。”
