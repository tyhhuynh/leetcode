class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        directions = [ (1,0), (-1,0), (0,1), (0,-1) ]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0: # base case: tile = 0
                    queue.append((i, j))
                else: # mark coordinates of tiles = 1 as unvisited (infinity)
                    mat[i][j] = math.inf

        while queue:
            i,j = queue.popleft() # removes leftmost (first) coordinate

            for di, dj in directions:
                ni, nj = i + di, j + dj # explores all directions of tile

                if 0 <= ni < rows and 0 <= nj < cols: # checks bounds of each new tile
                    if mat[ni][nj] == math.inf: # current coordinates are unvisited (infinity)
                        # increment coordinates and append it to queue
                        mat[ni][nj] = mat[i][j] + 1 # unvisited tile = current tile + 1
                        queue.append((ni, nj))
        
        return mat
            