# First Approach :- O(N)
# Curr as head, prev as None,Calculate length of LL, /2 that is till where youll run the loop
# Reverse the list, but keep head constant
# Beats 5.03%




class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = curr = head
        prev = None
        n = 0

        while temp:
            n+=1
            temp = temp.next

        while curr:
            curx = curr.next
            curr_copy = ListNode(curr.val, prev) 
            prev = curr_copy
            curr = curx
        
        tar = 0

        while head and (n/2)>=0:
            maxs = head.val + prev.val
            tar = max(maxs,tar)
            head = head.next
            prev = prev.next
            n-=1
        
        return tar
