#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

#%%
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        
        
# @lc code=end

#%%
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))

# %%

# 题目经验总结：
# 1) 核心模型：补数查询（complement）
#    对当前数字 x，只需要问：target - x 是否已经出现过。
#
# 2) 最优做法：哈希表一次遍历
#    用 seen 记录“数字 -> 下标”，查找补数可达 O(1) 平均复杂度。
#
# 3) 关键顺序：先查后存
#    if need in seen 要放在 seen[x] = i 前面，避免同一个元素被重复使用。
#
# 4) 复杂度结论：
#    时间 O(n)，空间 O(n)。
#
# 5) 常见易错点：
#    - 把 in 用在 values 上导致退化；这里要查 key（need in seen）。
#    - 返回的是下标，不是数字本身。
#    - 题目保证有解时，不需要额外处理“无解分支”。
