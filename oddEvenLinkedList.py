# First Approach:-  O(N)
# Check if the LL has at least 3 elements if not then return head, already sorted. Set oddlist as head and evenlist as head.next. 
# Traverse through curr, if you hit an oddposition set oddlist.next as curr and if you hit an even position set evenlist.next as curr.
# Increment both in both cases
# Beats 56.96%



class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next or not head.next.next:
            return head
            
        oddlist = curr = head
        evenlist = evenhead = head.next

        i = 1
        
        while curr:
            if i >2 and i%2!=0:
                oddlist.next = curr
                oddlist = oddlist.next
            elif i>2 and i%2 == 0:
                evenlist.next = curr
                evenlist = evenlist.next
            
            curr = curr.next
            i+=1
        
        evenlist.next = None
        oddlist.next = evenhead

        return head