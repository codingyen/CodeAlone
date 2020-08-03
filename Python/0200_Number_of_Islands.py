"""
Key point: 
- Locate a '1' first and make all the right, left, up and down to '0'.
- Make all the adjacent '1' to '0' so all the islands would be counted.
"""
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        if x != 0:
            self.dfs(grid, row, col, x - 1 , y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)

if __name__ == "__main__":
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    s = Solution()
    print(s.numIslands(grid))