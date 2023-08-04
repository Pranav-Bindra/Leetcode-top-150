#FirstApproach O(N)
#Check whether strings are equal, if yes:- return. Assign gcd to the smallest of the two strings and tar to the other.
#Check if gcd is indeed the gcd for target and gcd, if yes return, if not reduce length and then check
# Beats 49.86%

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        res = ''
        gcd = min([str1, str2], key=len)
        tar = max([str1, str2], key=len)


        for i in range(len(gcd),0,-1):
            if gcd[:i] == tar[:i] and tar[i:i+i] == tar[:i]:
                res = gcd[:i]
                k = int(len(tar)/len(res))
                print(res*k)
                l = int(len(gcd)/len(res))
                print(res*l)
                if res*k  == tar and res*l == gcd:
                    return res
        
        return ""