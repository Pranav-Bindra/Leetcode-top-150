# First Approach:- O(N)
# Basic, for loop add and check if its greater or equal to max
# Beats 89.62%

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        x = max(candies)

        for i in range(len(candies)):
            if candies[i]+ extraCandies >= x:
                res.append(True)
            else:
                res.append(False)

        return res