from typing import List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        d = {}

        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            d[cur].next = d.get(cur.next)
            d[cur].random = d.get(cur.random)
            cur = cur.next
        return d[head]