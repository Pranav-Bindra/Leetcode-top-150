# O(N) Approach
# Remove corner cases, 2 pointers with start and end, convert to list because immutable in python, 4 combinations where vowels can be present
# Beats 73.24%


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        start = 0
        end = len(s)-1
        res = ''

        if len(s)==1:
            return s

        s = list(s)
        while start<end:
            if s[start] not in vowels and s[end] not in vowels:
                start += 1
                end -=1
            elif s[start] in vowels and s[end] not in vowels:
                end -= 1
            elif s[start] not in vowels and s[end] in vowels:
                start += 1
            elif s[start] in vowels and s[end] in vowels:
                s[start],s[end] = s[end],s[start]
                start +=1
                end-=1
        
        return "".join(s)
