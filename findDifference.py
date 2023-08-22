# First Solution :- O(N+M)
# 2 lists, check if element exists in the other one using for loop, take list of set as output
# Beats 19.93%

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        ans2 = []
        for i in nums1:
            if i not in nums2:
                ans1.append(i)

        for j in nums2:
            if j not in nums1:
                ans2.append(j)

        return [list(set(ans1)),list(set(ans2))]
    
# Second Solution
# Pretty straight forward
# Beats 69.77%

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        return [list(s1-s2),list(s2-s1)]