# First Approach :- O(N)
# set 2 pointers, prev and curr. Reversee the next and return prev
# Beats 97.68% 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev  = None
        curr = head

        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev