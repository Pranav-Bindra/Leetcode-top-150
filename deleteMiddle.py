# First Attempt :- O(N)
# If head is none, return None, if head.next is None return hed.next. count total nodes, set middle as count//2-1. When you reach the element make next point to the next next element.
# Beats 53.18%



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head.next

        count = 0
        temp = head

        while temp!=None:
            count+=1
            temp = temp.next
        
        count = (count//2) - 1
        
        ptr = 0
        temp = head
        while temp is not None:
            if ptr == count:
                temp.next = temp.next.next
                break
            else:
                ptr+=1
                temp = temp.next
        
        return head