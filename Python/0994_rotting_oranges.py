import collections

class Solution:
    def orangeRotting(self, grid):
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            step += 1
        if fresh:
            return -1
        return step - 1

if __name__ == '__main__':
    grid = [[2,1,1], [1,1,0], [0,1,1]]
    s = Solution()
    print(s.orangeRotting(grid))