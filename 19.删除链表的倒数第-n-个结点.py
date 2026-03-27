#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
#%%
# 本地运行所需定义（提交到 LeetCode 时可忽略）
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    cur = head
    while cur:
        values.append(cur.val)
        cur = cur.next
    return values


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        fast, slow = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
# @lc code=end


if __name__ == "__main__":
    # 从测试角度设计：
    # 1) 常规删除中间节点，验证主流程
    # 2) 删除尾节点，验证 fast/slow 走位边界
    # 3) 删除头节点（n==len），验证 dummy 处理边界
    # 4) 单节点删除，验证最小规模输入
    # 5) 两节点删除第2个（头），再次覆盖头删场景
    test_cases: List[Tuple[List[int], int, List[int], str]] = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5], "常规场景：删除中间节点"),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4], "边界场景：删除尾节点"),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5], "边界场景：删除头节点"),
        ([1], 1, [], "最小规模：单节点删除"),
        ([1, 2], 2, [2], "小规模边界：两节点删除头节点"),
    ]

    s = Solution()
    all_passed = True

    for i, (arr, n, expected, reason) in enumerate(test_cases, start=1):
        head = build_linked_list(arr)
        result_head = s.removeNthFromEnd(head, n)
        result = linked_list_to_list(result_head)
        ok = result == expected
        all_passed = all_passed and ok
        print(
            f"Case {i}: {'PASS' if ok else 'FAIL'} | input={arr}, n={n}, "
            f"expected={expected}, got={result} | {reason}"
        )

    print("\n总结：", "全部通过" if all_passed else "存在失败用例")


# ===== 经验教训总结（复盘）=====
# 1) 看到“倒数第 n 个”优先联想双指针：
#    让 fast 先走 n 步，再与 slow 同时走，直到 fast 到尾部，
#    slow 就会停在“目标节点前驱”。
#
# 2) 看到“删除链表节点”优先联想 dummy：
#    删除操作本质是改前驱的 next，dummy 能统一“删头节点”和“删中间节点”逻辑。
#
# 3) 写链表题要先想清楚不变量：
#    整个过程中保持 fast 与 slow 间隔为 n，循环结束时 slow 正好指向待删节点前一个。
#
# 4) 测试要覆盖边界，而不只测常规：
#    - 删除中间节点（主流程）
#    - 删除尾节点（n=1）
#    - 删除头节点（n=len）
#    - 最小规模（单节点）
#
# 5) 工程化习惯：
#    本地补齐 ListNode + 构造/反构造工具 + 自测入口，
#    能在提交前快速验证正确性并减少调试时间。
