# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #cycle if the fast and slow pointer hit each other
        cur = head
        seen = set()
        
        while cur:
            if cur in seen:
                return cur
            seen.add(cur)
            cur = cur.next
        
        return None