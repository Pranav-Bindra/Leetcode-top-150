# O(N) Compulsory
# Create pre and post, 3 arrays, populate with prefix and postfix multiplication, then append to output.
# Beats 90.91%


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        prefix = []
        postfix = []
        output = []
        
        #[1,2,3,4] =  pre :- [1,2,6,24] post :- [24,24,12,4] op:- [24,12,8,6]

        for i in range(len(nums)):
            prod = pre*nums[i]
            prefix.append(prod)
            pre = prod

        for j in range(len(nums)-1,-1,-1):
            prod = post*nums[j]
            postfix.append(prod)
            post = prod
        
        postfix.reverse()
        output.append(postfix[1])

        for i in range(1,len(nums)-1):
            output.append(prefix[i-1]*postfix[i+1])

        output.append(prefix[-2])

        return output