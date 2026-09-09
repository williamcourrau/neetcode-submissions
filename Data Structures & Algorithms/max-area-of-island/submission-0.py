class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0:
                return 0
            
            if r >= rows or c >= cols:
                return 0 
            
            if (r,c) in visited:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            return 1 + (dfs(r + 1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
            
        for r in range(rows):
             for c in range(cols):
                  area = dfs(r,c)
                  max_area = max(max_area, area)

        return max_area
            

