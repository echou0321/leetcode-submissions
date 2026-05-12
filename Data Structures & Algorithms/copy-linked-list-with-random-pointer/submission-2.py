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
        nodeCopies = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            nodeCopies[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = nodeCopies[curr]
            copy.next = nodeCopies[curr.next]
            copy.random = nodeCopies[curr.random]
            curr = curr.next
        return nodeCopies[head]





