# First Approach :- O(N)
# 2 pointers sliding window, one at start one at end, calculate area of water, if i<j i+=1 else j-=1.
# Beats 95.03%


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0

        while i < j:
            width = j - i
            area1 = min(height[i], height[j]) * width

            if area1 > area:
                area = area1

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area