#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                p = head
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        return None
                
        
        
# @lc code=end

# 解题思路（Floyd 快慢指针）：
# 1) 先判环：
#    - slow 每次走 1 步，fast 每次走 2 步。
#    - 若 fast 或 fast.next 为空，说明无环，返回 None。
#    - 若 fast 与 slow 相遇，说明有环，并得到第一次相遇点。
#
# 2) 再找入口：
#    - 令指针 p 从 head 出发，slow 留在第一次相遇点。
#    - p 与 slow 同时每次走 1 步，再次相遇的节点就是环入口。
#
# 核心结论：
# - 设 head 到入口距离为 a，入口到首次相遇点距离为 b，环长为 c，
#   可推出 a = (k-1)c + (c-b)，因此从 head 与相遇点同速前进会在入口相遇。
#
# 复杂度：
# - 时间 O(n)
# - 空间 O(1)
