# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        result = dummy
        while l1 or l2 or carry: 
            l1val = 0
            if l1: 
                l1val = l1.val
            
            l2val = 0
            if l2: 
                l2val = l2.val

            total = l1val + l2val + carry
            if total >= 10: 
                carry = 1
                digit = total - 10
            else: 
                carry = 0
                digit = total
            
            dummy.next = ListNode(digit)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next
            
        return result.next