# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#链表具有递归性，所以每个链表节点是一个类，类里包含.val和.next，其中.next指向下一个节点，下一个节点作为类同样包含.val和.next，以此类推。。。
class Solution:
    def addTwoNumbers(self, l1, l2):
    	#定义一个链表，表头值为零
        l3 = ListNode(0)
        #将l3赋值给dummy，并将dummy.next作为返回值
        dummy = l3
        #进位数，每10进一，初始为0
        add = 0
        #满足其中一个条件即运行，l1的当前节点存在；l2的当前节点存在；存在进位
        while (l1 !=None or l2 !=None or add != 0):
            if (l1 == None):
                l1 = ListNode(0)
            if (l2 == None):
                l2 = ListNode(0)
            current = l1.val + l2.val + add
            l1 = l1.next
            l2 = l2.next
            add = 0
            #判断是否进位
            if current >= 10:
                add = 1
                current = current % 10
            #为下个节点添加新节点
            l3.next = ListNode(current)
            l3 = l3.next
        #最后返回虚拟节点的下一个节点开始的链表
        return dummy.next