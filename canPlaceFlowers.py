# First Approach :- O(N)
# Check for every corner case, if len = 1, if at start, at end pretty easy after that
# Beats 90.68%

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start = 0
        end = len(flowerbed)-1
        if len(flowerbed) == 1 and flowerbed[0]==0 and n==1:
            return True

        for i in range (len(flowerbed)):
            if n == 0:
                return True
            elif flowerbed[i] == 1:
                pass
            elif i == start and flowerbed[i+1] == 0 and flowerbed[i]==0:
                n=n-1
                flowerbed[i] = 1
            elif i == end and flowerbed[i-1]==0 and flowerbed[i] == 0 :
                n=n-1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n = n-1
                flowerbed[i] = 1
        
        if n==0:
            return True
        else:
            return False