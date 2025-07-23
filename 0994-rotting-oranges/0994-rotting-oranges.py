class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # multi-source BFS
        # track initial # of fresh oranges
        queue = deque()
        time, fresh = 0, 0
        
        # initializes information about # of oranges & coords of rotting orange(s)
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while queue and fresh > 0:

            for i in range(len(queue)): # allows for rotting to occur 'every minute' and increments time end of for-loop
                r, c = queue.popleft()
                for drow, dcol in directions:
                    row, col = drow + r, dcol + c

                    # checks if row/col out of bounds or current cell not fresh
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    queue.append([row, col]) # appends adjacent oranges that rotted
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

        