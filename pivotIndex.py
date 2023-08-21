# Brute Force
# Consider left-most index as pivot first and keep calculating the left and right sums till you find the pivot. 
# Inconsisten solution but logic is correct. Timit Limit Exceeded


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot  = 0

        while pivot<=len(nums)-1:
            sum_left = 0
            for i in range(pivot):
                sum_left = sum_left + nums[i]

            sum_right = 0
            for j in range(pivot+1,len(nums)):
                sum_right = sum_right + nums[j]

            if sum_left == sum_right:
                return pivot
            
            pivot+=1
        
        return -1
    

# Using prefix sum
# Consider the left most element as the pivot, insert a 0 at the start of nums, check if it is indeed the pivot and then return
# Beats 89.49%

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot  = 1
        sum_right = sum(nums)
        sum_left = 0
        nums.insert(0,0)

        while pivot<=len(nums)-1:
            sum_left = sum_left + nums[pivot-1]

            sum_right = sum_right - nums[pivot]

            if sum_left == sum_right:
                return pivot-1
            
            pivot+=1
        
        return -1