public class Solution 
{
    public void islandsAndTreasure(int[][] grid) 
    {
        var rows = grid.Length;
        var cols = grid[0].Length;

        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c] == 0)
                {
                    DFS(grid, r, c, 0);
                }
            }
        }
    }

    private void DFS(int[][] grid, int r, int c, int movements)
    {
        if(r < 0 || c < 0 || r >= grid.Length || c >= grid[0].Length || grid[r][c] == -1 || grid[r][c] < movements)
        {
            return;
        }

        grid[r][c] = movements;

        DFS(grid, r + 1, c, movements + 1);
        DFS(grid, r - 1, c, movements + 1);
        DFS(grid, r, c+1, movements + 1);
        DFS(grid, r, c-1, movements + 1);
    }
}
