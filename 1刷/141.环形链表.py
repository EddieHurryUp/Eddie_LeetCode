#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None

# @lc code=start
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# @lc code=end
def build_linked_list(values: list[int], pos: int) -> Optional[ListNode]:
    """根据 values 构建链表；pos>=0 时尾节点指向第 pos 个节点形成环。"""
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


def run_tests() -> None:
    cases = [
        # (values, pos, expected)
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ]

    solver = Solution()
    for i, (values, pos, expected) in enumerate(cases, start=1):
        head = build_linked_list(values, pos)
        result = solver.hasCycle(head)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Case {i}: values={values}, pos={pos}, "
            f"expected={expected}, got={result} -> {status}"
        )


if __name__ == "__main__":
    run_tests()

# ===== 题目总结与经验 =====
# 1) 本题核心
# - 目标不是“找到环入口”，而是“判断是否有环”。
# - 快慢指针：slow 每次走 1 步，fast 每次走 2 步。
# - 若有环，fast 最终会在环内追上 slow；若无环，fast 或 fast.next 会先为 None。
#
# 2) 为什么可行（直觉版）
# - 把环看作跑道，fast 速度更快，只要都在跑道内运动，fast 一定会套圈追上 slow。
#
# 3) 常见易错点
# - 易错点 A：在循环一开始就判断 slow == fast，会把初始同一节点误判为有环。
#   正确做法：先移动指针，再比较是否相遇。
# - 易错点 B：while 条件不完整，必须写成 while fast and fast.next。
#
# 4) 复杂度
# - 时间复杂度：O(n)
# - 空间复杂度：O(1)
#
# 5) 测试经验（面试可口述）
# - 正常用例：有环（如 [3,2,0,-4], pos=1）应返回 True。
# - 边界用例：单节点无环（[1], pos=-1）应返回 False。
# - 极端用例：空链表（[]）应返回 False。
# - 补充用例：双节点成环（[1,2], pos=0）应返回 True。
