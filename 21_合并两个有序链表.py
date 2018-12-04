# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#将两个链表交叉拼接，并非题目意思
class Solution2:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        ss = dummy
        who = 1
        while l1 or l2:
            if who == 1:
                if l2:
                    who = 2
                if l1:
                    ss.next = ListNode(l1.val)
                    ss = ss.next
                    l1 = l1.next
            elif who == 2:
                if l1:
                    who = 1
                if l2:
                    ss.next = ListNode(l2.val)
                    ss = ss.next
                    l2 = l2.next
        return dummy.next

#原题解答
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        eles = []
        while l1:
            eles.append(l1.val)
            l1 = l1.next
        while l2:
            eles.append(l2.val)
            l2 = l2.next
        ss = dummy
        eles.sort()
        for ele in eles:
            ss.next = ListNode(ele)
            ss = ss.next
        return dummy.next




