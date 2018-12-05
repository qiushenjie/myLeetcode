# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定的有序链表： [-10, -3, 0, 5, 9],

# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

#用快慢指针解决,快指针一下走两步,慢指针走一步,当快指针走到结尾,
#慢指针刚好走到一半,然后将链表分为左右两段,然后递归上诉操作就可以拿到所以根节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.next.val)
        temp = slow.next
        slow.next = None #截断
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)
        return root



