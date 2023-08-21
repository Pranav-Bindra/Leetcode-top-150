# First Approach :- O(N)
# Make a list with 0 append the running sum and then select maximum
# Beats 66.07%

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt  = [0]
        sumx = 0

        for i in range(len(gain)):
            sumx = alt[i] + gain[i]
            alt.append(sumx)
        
        return max(alt)