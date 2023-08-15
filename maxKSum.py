# O(N) Sliding Window first approach
# Sort first, then piece of cake, just compare sumx and k and slide the window accordingly
# Beats 88.71%


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j = 0, len(nums)-1
        oper = 0
        sumx = 0
        nums.sort()

        while i<j:
            sumx = nums[i] + nums[j]
            if sumx == k:
                oper+=1
                i+=1
                j-=1
            elif sumx<k:
                i+=1
            else:
                j-=1

        
        return oper