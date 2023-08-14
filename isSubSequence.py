# First Approach : O(max(m, n))
# 2 pointers, both at start, counter set to len(s), keep checking, if match remove previous string from target, if counter = 0 in end, return true
# Beats 55.51%

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        counter = len(s)
        i,j = 0,0

        while i < len(s):
            while j < len(t):
                if t[j]==s[i]:
                    print(i,j)
                    counter-=1
                    if len(s) == 1:
                        return True
                    s = s[i+1:]
                    t = t[j+1:]
                    i = 0
                    j = 0
                else:
                    j+=1
            i+=1
        

        if counter==0:
            return True
        
# Second Approach : DP
# Create array dp as m+1,n+1 make table and follow same code
# Beats 5.55%

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
    
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n] == len(s)