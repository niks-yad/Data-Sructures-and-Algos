class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        bfsQ = []
        mins = -1
        check = False
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    check = True

        if check == False:
            return 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    bfsQ.append([r,c])

        while bfsQ:
            print(bfsQ)
            for i in range(len(bfsQ)):
                
                r = bfsQ[0][0]
                c = bfsQ[0][1]
                if r+1 < R:
                    if grid[r+1][c] == 1:
                        bfsQ.append([r+1,c])
                        grid[r+1][c] = 2
                if r > 0:
                    if grid[r-1][c] == 1:
                        bfsQ.append([r-1,c])
                        grid[r-1][c] = 2
                if c+1 < C:
                    if grid[r][c+1] == 1:
                        bfsQ.append([r,c+1])
                        grid[r][c+1] = 2
                if c > 0:
                    if grid[r][c-1] == 1:
                        bfsQ.append([r,c-1])
                        grid[r][c-1] = 2
                
                bfsQ.pop(0)
            
            mins += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1

        return mins
                
        