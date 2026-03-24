#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

# @lc code=end

# 知识点总结：
# 1) 题目本质：
#    把“字符集合相同、字符频次相同”的字符串分到同一组（字母异位词分组）。
#
# 2) 核心技巧（哈希分组）：
#    为每个字符串构造一个“唯一特征 key”，相同 key 的字符串放同一组。
#    本题 key 采用排序后字符串：key = "".join(sorted(s))
#    例如 "eat"、"tea"、"ate" 排序后都为 "aet"。
#
# 3) 数据结构选择：
#    defaultdict(list) 适合做分组容器，省去手动判断 key 是否存在。
#
# 4) 复杂度分析：
#    设 n 为字符串个数，k 为字符串平均长度。
#    时间复杂度：O(n * k log k)（每个字符串排序一次）
#    空间复杂度：O(n * k)（哈希表存储分组结果）
#
# 5) 易错点：
#    - 返回 list(groups.values())，不是返回整个字典。
#    - key 要稳定可哈希；常见写法是排序字符串或排序元组。
#    - 结果中每组顺序、组与组顺序通常不作要求（LeetCode 按内容判定）。
#
# 6) 进阶优化：
#    若字符串只含小写字母，可用 26 位计数数组转 tuple 作为 key，
#    可将单字符串处理降为 O(k)，避免排序的 log k 因子。
