# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。

# 示例:

# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

'''
如示例，做法是抽出2指向空，抽出3指向2，抽出4指向3，最后先将2指向5，再将1指向4，因为在此之前1都是指向2的
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        dummy = ln = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1): #最终指向第m个的前一个
            pre = pre.next
        curr = pre.next #指向第m个，在循环结束后后会指向第n+1个
        tmp = None #倒叙在接下来会存于tmp中
        for i in range(n - m + 1):
            nextcurr = curr.next
            curr.next = tmp
            tmp = curr 
            curr = nextcurr
        pre.next.next = curr #先指向第n+1个,pre.next指向的是原先第m个数,因为在此之前m-1都是指向m的
        pre.next = tmp
        return dummy.next

