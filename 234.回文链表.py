#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next 
            slow.next = pre
            pre = slow
            slow = next
            
        if fast:
            slow = slow.next
        
        while pre:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next

        return True
        


# @lc code=end

