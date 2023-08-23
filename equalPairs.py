# First Approach :- O(N^2)
# Create a row_grid and col_grid and compare them.
# Beats 42.76%


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_grid = []
        col_grid = []
        
        for i in range(len(grid)):
            row_grid.append(tuple(grid[i]))

        for i in range(len(grid)):
            col = []
            for j in range(len(grid[i])):
                col.append(grid[j][i])
            col_grid.append(tuple(col))
        
        output = 0
        
        for i in row_grid:
            for j in col_grid:
                if i == j:
                    output += 1
        
        return output