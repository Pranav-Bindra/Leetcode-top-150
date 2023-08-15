# First Approach :- O(N*K)
# Not using sliding window, using 2 pointers, time limit exceeds but logic is correct

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        print(len(nums))
        i = 0
        sumx = -99999999999999

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == k:
            return sum(nums)/k

        while i<=len(nums)-k:
            sumy = sum(nums[i:k+i])
            i+=1
            sumy = max(sumx,sumy)
            sumx = sumy

        return sumy/k
    

# Second Approach :-  O(N)
# Sliding window, calcaulate sum upto k first, then slide the window ie subtract earlier number and add the next, reduces total operations.
# Beats 96.11%

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        sumx = sum(nums[:k])
        lst = [sumx]

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == k:
            return sum(nums)/k

        for i in range (1,len(nums)-k+1):
            sumx = sumx - nums[i-1]
            sumx = sumx + nums[i+k-1]
            lst.append(sumx)

        return (max(lst)/k)