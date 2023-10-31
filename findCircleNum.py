# O(N)
# have a visited tracker set as false initially,initialize prov to 0, if visited is False, dfs on visited and its neighbors
# Beats 95.88%

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j]!= True:
                    dfs(j)



        n = len(isConnected)
        visited = [False]*n
        prov = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                prov+=1
        
        return prov


