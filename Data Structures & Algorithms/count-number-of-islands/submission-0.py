class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        number_islands = 0

        def dfs(r, c):
            if r >= ROWS or r < 0:
                return

            if c >= COLS or c < 0:
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"  # visited

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    number_islands += 1

        return number_islands



        