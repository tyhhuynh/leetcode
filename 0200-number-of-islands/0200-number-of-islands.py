class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])

        if not grid:
            return 0
        
        visited = set() # tracks coords. and prevents cycles
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    # checks grid[r][c] in bounds, is an island, & not visited
                    if (r in range(ROWS) and 
                        c in range(COLS) and 
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                            queue.append((r, c))
                            visited.add((r, c))

        # iterative solution
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands