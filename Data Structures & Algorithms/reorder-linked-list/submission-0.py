# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use slow and fast pointer to find halfway point
        cur = head
        slow = cur
        fast = cur.next
        while fast != None and fast.next != None: 
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        # Reverse the second half of the linked list
        prev = None
        while head2 != None: 
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        # Merge the two linked lists
        arr1 = head
        arr2 = prev

        while arr1 != None and arr2 != None: 
            temp1 = arr1.next
            temp2 = arr2.next
            arr1.next = arr2
            arr2.next = temp1
            arr1 = temp1
            arr2 = temp2
