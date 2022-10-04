# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating a dummy node
        dummy = ListNode()
        
        #pointer to the dummy
        tail = dummy
        
        #while not at end of either linked list
        while list1 and list2:
            
            #if list1 val is smaller, point dummy node to the list 1
            if list1.val < list2.val:
                tail.next = list1
                
                #update the pointers
                list1 = list1.next
                tail = tail.next

            #if list2 val is smaller or equal, point it to list2 
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return dummy.next