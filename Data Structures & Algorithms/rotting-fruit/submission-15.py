class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #first we count rotten oranges by
            #visit the graph
        #level order multi source BFS
        #return if number of level order iternation if no fresh, else -1

        q = deque()
        fresh = 0
        
        ROWS = len(grid)
        COLS = len(grid[0])

        #counting rotten and fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        #multi source BFS
        minutes = 0
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()

                #infect
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1




