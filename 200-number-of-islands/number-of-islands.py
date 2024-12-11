from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        results = 0
        islands = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    results += 1
                    islands.append((i,j))

                    while islands:
                        y, x = islands.popleft()

                        if x - 1 >= 0:
                            if grid[y][x-1] == "1":
                                grid[y][x-1] = "0"
                                islands.append((y,x-1))
                        if x + 1 < len(grid[0]):
                            if grid[y][x+1] == "1":
                                grid[y][x+1] = "0"
                                islands.append((y,x+1))
                        if y - 1 >= 0:
                            if grid[y-1][x] == "1":
                                grid[y-1][x]= "0"
                                islands.append((y-1,x))
                        if y + 1 < len(grid):
                            if grid[y+1][x] == "1":
                                grid[y+1][x] = "0"
                                islands.append((y+1,x))

        return results