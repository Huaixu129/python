from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:   # 检查是否两个链表都为空
            return None
        if not l1:
            l1 = ListNode(0, None)
        elif not l2:
            l2 = ListNode(0, None)

        m = l1.val + l2.val
        l1.val = m % 10
        if l1.next:
            l1.next.val = l1.next.val + m // 10
        else:
            l1.next = ListNode(m // 10, None) if m // 10 else None
        l1.next = self.add_two_numbers(l1.next, l2.next)
        return l1
