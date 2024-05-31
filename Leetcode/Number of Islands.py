class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islandCount = 0
        R = len(grid)
        C = len(grid[0])
        def bfs(r,c):
            nonlocal R
            nonlocal C
            if grid[r][c] == '1':
                grid[r][c] = '2'
            else:
                return

            if r+1 < R:
                if grid[r+1][c] == '1':
                    bfs(r+1,c)
            if r > 0:
                if grid[r-1][c] == '1':
                    bfs(r-1,c)
            if c+1 < C:
                if grid[r][c+1] == '1':
                    bfs(r,c+1)
            if c > 0:
                if grid[r][c-1] == '1':
                    bfs(r,c-1)


        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == '1':
                    bfs(r,c)
                    islandCount += 1

        return islandCount