class Solution:
    def numDistinctIslands(self, grid):
        def dfs(r, c, di = 0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] > 0):
                grid[r][c] *= -1
                island.append(di)
                dfs(r+1, c, 1)
                dfs(r-1, c, 2)
                dfs(r, c+1, 3)
                dfs(r, c-1, 4)
                island.append(0)

        islands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                island = []
                dfs(r, c)
                if island:
                    islands.add(tuple(island))

        return len(islands)

        """
        row = len(grid)
        col = len(grid[0])
        directions = {'l' : [-1, 0], 'r' : [1, 0],  'u' : [0, 1], 'd' : [0, -1]}

        def dfs(i, j, grid, island):
            if not ( 0 <= i < row and 0 <= j < col and grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            for k, v in directions.items():
                island.append(k)
                dfs(i + v[0], j + v[1], grid, island)
            return True


        islands = set()
        for i in range(row):
            for j in range(col):
                island = []
                if dfs(i, j, grid, island):
                    islands.add("".join(island))
        return len(islands)
        """

if __name__ == '__main__':
    grid = [[1, 1, 0],
            [0, 1, 1], 
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0]]

    s = Solution()
    print(s.numDistinctIslands(grid))
