# Brute Force :- O(N*K)
# Time Limit Exceeded, but syntatically correct

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        count_vow = []

        for i in range(len(s)-k+1):
            counter = 0
            lst = list(s[i:k+i])
            for i in lst:
                if i in vowels:
                    counter+=1
                
            count_vow.append(counter)
        
        return max(count_vow)

# Sliding window :- O(N)
# remember how to picl the last element and add it, remember till where to slide.
# Beats 5.01%


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        lst = list(s[:k])
        counter = 0
        for i in lst:
            if i in vowels:
                counter+=1
        count_vow = [counter]

        for i in range(1,len(s)-k+1):
            x = lst.pop(0)
            char = s[i+k-1]
            lst.append(char)
            if x in vowels and char not in vowels:
                counter-=1
            elif x not in vowels and char in vowels:
                counter+=1
            else:
                pass
                
            count_vow.append(counter)
        
        return max(count_vow)
