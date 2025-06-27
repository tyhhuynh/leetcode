class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # base case:
        ogColor = image[sr][sc]
        if ogColor == color:
            return image
        
        # recursive case
        def dfs(r, c):
             # helper fn: checks bounds & color of starting pixel != target color
            if (0 <= r < len(image)) and (0 <= c < len(image[0])) and image[r][c] == ogColor:
                image[r][c] = color # changes current pixel to target color

                # recursively calls itself on adjacent pixels
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
            