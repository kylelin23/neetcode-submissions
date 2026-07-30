# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        while head2: 
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        half1 = head
        half2 = prev
        while half2: 
            temp1 = half1.next
            temp2 = half2.next
            half1.next = half2
            half2.next = temp1
            half1 = temp1
            half2 = temp2
