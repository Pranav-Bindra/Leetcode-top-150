# First Approach :- O(N) + K*O(LOG(N))
# Convert to heap using heapify, done in place. Keep popping till k, return popped eleemnt 
# Beats 26.18%


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        for i in range(k):
            x = heapq.heappop(nums)
        
        return -x