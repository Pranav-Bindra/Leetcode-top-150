# First Attempt :- O(N)
# Traverse the input arrray, if * is encountered delete the previous element, if not append the character
# Beats 93.99% 

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i == '*':
                del stack[-1]
            else:
                stack.append(i)
        
        if stack:
            return ''.join(stack)
        else:
            return ''