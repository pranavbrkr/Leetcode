class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r not in range(m) or c not in range(n) or prev_height > heights[r][c]:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n - 1, atl, heights[i][n - 1])
        
        for i in range(n):
            dfs(0, i, pac, heights[0][i])
            dfs(n - 1, i, atl, heights[m - 1][i])
        
        answer = []
        for (r, c) in pac:
            if (r, c) in atl:
                answer.append([r, c])
        
        return answer