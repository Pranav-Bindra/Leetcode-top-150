# First Approach :- O(N)
# Sliding window, dynamic, start and end at 0 initally, check if 0,decrement change, if change goes below 0, increment start, indrement end store max_len
# Beats 72.73% 


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        start = 0 
        end = 0
        change = k

        while end < len(nums):
            if nums[end] == 0:
                change -= 1
            
            while change < 0:
                if nums[start] == 0:
                    change += 1
                start += 1
            
            end += 1 
            max_len = max(end-start, max_len)
        
        return max_len