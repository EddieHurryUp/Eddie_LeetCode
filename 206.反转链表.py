#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表

#%%
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        
# @lc code=end


def build_linked_list(nums):
    dummy = ListNode()
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
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = Solution().reverseList(head)
    print(linked_list_to_list(new_head))  # [5, 4, 3, 2, 1]


# 题目知识点总结（206.反转链表）：
# 1) 题目本质：
#    把每个节点的 next 指针方向反过来，返回新的头节点。
#
# 2) 核心思路（迭代三指针）：
#    - prev：已反转部分的头
#    - cur：当前待处理节点
#    - nxt：暂存 cur 的下一个节点（防止断链）
#    每轮步骤固定：先存 nxt -> 反转 cur.next -> 前移 prev/cur。
#
# 3) 关键不变量：
#    - prev 始终指向“已经反转好”的链表头
#    - cur 始终指向“尚未处理”的链表头
#    循环结束时 cur 为 None，prev 即最终答案。
#
# 4) 复杂度：
#    时间 O(n)，每个节点只访问一次；
#    空间 O(1)，只使用常数个额外指针。
#
# 5) 易错点：
#    - 忘记先保存 nxt，导致后续链表丢失。
#    - 指针更新顺序写错（应先保存、再反转、再前移）。
#    - 返回值应是 prev，不是原 head。
#
# 6) 类型注解补充：
#    Optional[ListNode] 表示参数/返回值可能是 ListNode，也可能是 None（空链表）。
