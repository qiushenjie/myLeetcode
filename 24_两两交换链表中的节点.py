# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 示例:

# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 说明:

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        ss = dummy
        who = 2
        if not head:
            return []
        if not head.next:
            return head
        l1 = head
        l2 = head.next
        while l1 or l2:
            if who == 1:
                if l2:
                    who = 2
                if l1:
                    ss.next = ListNode(l1.val)
                    ss = ss.next
                    if l1.next:
                        l1 = l1.next.next
                    elif not l1.next:
                        l1 = l1.next
            elif who == 2:
                if l1:
                    who = 1
                if l2:
                    ss.next = ListNode(l2.val)
                    ss = ss.next
                    if l2.next:
                        l2 = l2.next.next
                    elif not l2.next:
                        l2 = l2.next
        return dummy.next


