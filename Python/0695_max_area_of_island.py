class Solution:
    def maxAreaOfIsland(self, grid):
        row = len(grid)
        col = len(grid[0])
        self.maxArea = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.area = 0
                    self.dfs(grid, row, col, i, j)
        return self.maxArea

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == 0:
            return
        grid[x][y] = 0
        self.area += 1
        self.maxArea = max(self.maxArea, self.area)
        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)




if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    s = Solution()
    print(s.maxAreaOfIsland(grid))