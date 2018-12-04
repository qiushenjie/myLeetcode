# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def add():


class Solution1:
    def removeNthFromEnd(self, head, n):
        count = 1
        dummy = head
        curr = head
        while curr.next:
            count += 1
            curr = curr.next
        if count == 1:
            return []
        if count == n: #删除第一个，直接返回node.next
            return dummy.next
        if count == 2 and n == 1:
            dummy.next = None
            return dummy
        N = count - n 
        for i in range(count - 1):
            if i != N-1:
                head = head.next
            if i == N-1:
                if head.next.next: #n = 2时
                    head.next = head.next.next
                    head = head.next
                elif head.next: #n = 1时
                    head.next = None
                else:
                    break
        return dummy


class Solution:
    def removeNthFromEnd(self, head, n):
        #相互追赶，快的比慢的多跑n步，之后再一起跑，快的到终点后都停下来，慢的直接跨过后一个到再下一个
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
s = ListNode(1)
a = s
a.next = ListNode(3)
a.next.next = ListNode(4)
#a.next.next.next = ListNode(5)
#a.next.next.next.next = ListNode(6)





