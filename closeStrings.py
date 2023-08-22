# First Solution :- O(N)
# If length is not equal, return False, if distinct characters vary, return False, if the position and the value match, return True else return False 
# Beats 78.17%

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        tracker1 = Counter(word1)
        tracker2 = Counter(word2)
        
        chars1 = set(tracker1.keys())
        chars2 = set(tracker2.keys())
        
        if chars1 != chars2:
            return False
        
        
        return sorted(tracker1.values()) == sorted(tracker2.values()) and sorted(tracker1.keys()) == sorted(tracker2.keys())
