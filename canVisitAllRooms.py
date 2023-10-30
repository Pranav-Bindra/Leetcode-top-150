# o(n)
# Initialize a set, visited. dfs on the list rooms, if already visited ignore if not, dfs on that room
# return true if length of visited matches length of room
# Beats 24.55%

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited  = set()

        def dfs(room):
            visited.add(room)

            for i in rooms[room]:

                if i not in visited:
                    dfs(i)

        
        dfs(0)
        return len(visited) == len(rooms)


        
            
        
        