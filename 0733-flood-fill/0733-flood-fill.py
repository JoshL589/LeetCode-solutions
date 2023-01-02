class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_colour = image[sr][sc]
        row = len(image[0])
        col = len(image)
        seen = set()
        def dfs(sr, sc):
            if 0 <= sr < col and 0 <= sc < row and image[sr][sc] == starting_colour and (sr,sc) not in seen:
                seen.add((sr,sc))
                image[sr][sc] = color
                dfs(sr+1, sc)
                dfs(sr-1, sc)
                dfs(sr, sc+1)
                dfs(sr, sc-1)
        dfs(sr, sc)
        return image