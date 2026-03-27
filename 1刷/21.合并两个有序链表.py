#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

from typing import Optional
class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p1 if p1 else p2
        return dummy.next
            

        
# @lc code=end

def build_linked_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == "__main__":
    s = Solution()

    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    print(linked_list_to_list(s.mergeTwoLists(l1, l2)))  # [1, 1, 2, 3, 4, 4]

    l3 = build_linked_list([])
    l4 = build_linked_list([])
    print(linked_list_to_list(s.mergeTwoLists(l3, l4)))  # []

# 题目经验总结（21.合并两个有序链表）：
# 1) 核心模型：双指针 + 虚拟头结点（dummy）
#    - p1、p2 分别指向两条有序链表的当前节点。
#    - 每轮取较小值节点接到结果链表尾部，随后对应指针后移。
#
# 2) 为什么要用 dummy：
#    - 避免处理“第一个节点”的特殊分支，统一拼接逻辑。
#    - 最后直接返回 dummy.next 即可。
#
# 3) 关键收尾：
#    - 当一条链表先走完，另一条剩余部分本身有序，可直接整体挂到 cur.next。
#
# 4) 复杂度分析：
#    - 时间复杂度 O(m + n)：每个节点最多被访问一次。
#    - 空间复杂度 O(1)：只使用常数级额外指针（不计输出链表本身）。
#
# 5) 常见易错点：
#    - 忘记在循环内移动 cur，导致链表连接错误。
#    - 收尾时漏接剩余链表。
#    - 返回 dummy 而不是 dummy.next。
#
# 6) 面试描述模板（可直接复述）：
#    “我用两个指针同步遍历两条有序链表，每次把较小节点接到结果尾部，
#    并推进对应指针。循环结束后把未遍历完的那条链表直接接上。
#    为了统一边界处理，我使用虚拟头结点。整体时间 O(m+n)，空间 O(1)。”
