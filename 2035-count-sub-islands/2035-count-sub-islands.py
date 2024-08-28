class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m, n = len(grid1), len(grid1[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid2[i][j] == 0 or visited[i][j]:
                return True
            elif grid2[i][j] == 1 and grid1[i][j] == 0:
                return False
            else:
                visited[i][j] = True
                down = dfs(i + 1, j)
                up = dfs(i - 1, j)
                right = dfs(i, j + 1)
                left = dfs(i, j - 1)
                
                return up and down and left and right
        
        answer = 0

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid2[i][j] == 1:
                    if dfs(i, j):
                        answer += 1

        return answer