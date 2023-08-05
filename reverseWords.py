# First Approach :- O(N)
# split the string, check where both are words without spaces, reverse, strip of extra spaces and remove spaces in between
# Beats 82.21%

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        mod = s.split(' ')
        start = 0
        end = len(mod)-1
        while start < end:
            if mod[start] != ' ' and mod[end] != ' ':
                mod[start],mod[end] = mod[end],mod[start]
                start+=1
                end -=1
            
            if mod[start] != ' ' and mod[end] == ' ':
                end-=1

            if mod[start] == ' ' and mod[end] != ' ':
                start+=1
            
            if mod[start]== ' ' and mod[end] == ' ':
                start+=1
                end-=1
    
        x=[j for i,j in enumerate(mod) if j!='']

        return ' '.join(x)