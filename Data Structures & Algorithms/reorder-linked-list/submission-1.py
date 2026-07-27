# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next
        while fast != None and fast.next != None: 
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        
        prev = None
        while head2 != None: 
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        start1 = head
        start2 = prev
        while start1 != None and start2 != None: 
            temp1 = start1.next
            temp2 = start2.next
            start1.next = start2
            start2.next = temp1
            start1 = temp1
            start2 = temp2