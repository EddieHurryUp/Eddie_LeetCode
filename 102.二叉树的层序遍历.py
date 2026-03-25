#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
from typing import List,Optional
from collections import deque

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans
        
# @lc code=end

# 题目知识点总结（102.二叉树的层序遍历）：
# 1) 题目本质：
#    按层从上到下、从左到右遍历二叉树，典型 BFS（广度优先搜索）。
#
# 2) 核心数据结构：
#    使用 deque 作为队列：
#    - 入队：append
#    - 出队：popleft
#    这两步都是 O(1)。
#
# 3) 分层关键技巧：
#    每轮 while 开始先记录 level_size = len(q)，
#    表示“当前层节点数”，只循环 level_size 次。
#    这样本层新增的子节点会留到下一层处理，不会混层。
#
# 4) 处理流程：
#    - 空树直接返回 []
#    - 根节点入队
#    - 循环：弹出本层节点、收集 node.val、把左右孩子入队
#    - 本层结束后把 level 加入答案
#
# 5) 复杂度：
#    时间 O(n)：每个节点仅入队出队一次
#    空间 O(n)：最坏情况下队列会存一整层节点
#
# 6) 易错点：
#    - 忘记空树判断
#    - 不锁定 level_size 导致层级混乱
#    - 使用 list.pop(0) 导致性能退化
