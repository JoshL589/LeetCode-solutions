class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_colour = image[sr][sc]
        row = len(image[0])
        col = len(image)
        seen = set()
        def dfs(y, x):
            if 0 <= x < row and 0 <= y < col and image[y][x] == starting_colour and (y, x) not in seen:
                seen.add((y, x))
                image[y][x] = color
                dfs(y + 1, x)
                dfs(y - 1, x)
                dfs(y, x+1)
                dfs(y, x-1)
        dfs(sr, sc)
        return image