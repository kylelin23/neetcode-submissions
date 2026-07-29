"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCur = {None: None}
        cur = head
        while cur: 
            oldToCur[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur: 
            oldToCur[cur].next = oldToCur[cur.next]
            oldToCur[cur].random = oldToCur[cur.random]
            cur = cur.next
        return oldToCur[head]