# First Solution :- O(N+M+K1+K2)
# Create counter hashmap, create occ list which consists count of occurances, if length of distinct values is equal to length of values that means no duplicates
# Beats 46.48%

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tracker = Counter(arr)
        occ = [i for i in tracker.values()]
        if len(set(occ)) == len(occ):
            return True
        else:
            return False