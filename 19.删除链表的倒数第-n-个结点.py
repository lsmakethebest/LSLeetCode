#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(0,head)
        slow = dummyHead
        fast = head
        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next 
            fast = fast.next

        slow.next = slow.next.next
        return dummyHead.next
# @lc code=end

