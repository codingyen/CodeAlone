class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        
        row = len(rooms)
        col = len(rooms[0])
        q = [(i, j) for i in range(row) for j in range(col) if rooms[i][j] == 0]
        
        for x, y in q:
            distance = rooms[x][y] + 1
            directions = [(-1, 0), (1, 0), (0, -1),  (0, 1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y)) 



if __name__ == "__main__":
    INF = 2147483647
    rooms = [
      [INF, -1, 0, INF],
      [INF, INF, INF, -1],
      [INF, -1, INF, -1],
      [0, -1, INF, INF]
    ]
    s = Solution()
    s.wallsAndGates(rooms)
    print(rooms)