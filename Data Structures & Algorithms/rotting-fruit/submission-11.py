class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1],[-1,0],[0,-1]]
        q = deque()
        fresh = 0
        time = 0
        #count the fresh and rotten ones
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c)) #as a tuple  #put the rotten ones in queue to process       
        while fresh > 0 and q:
            for i in range(len(q)): #the older populated q
                r, c = q.popleft()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (row in range(len(grid)) and
                        col in range(len(grid[0])) and
                        grid[row][col] == 1):

                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
       
        