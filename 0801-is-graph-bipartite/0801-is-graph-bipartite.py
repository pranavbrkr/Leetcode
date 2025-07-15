class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, col):
            color[node] = col

            for adj in graph[node]:
                if color[adj] == -1:
                    if not dfs(adj, not col):
                        return False
                elif color[adj] == col:
                    return False
            
            return True

        for node in range(n):
            if color[node] == -1:
                if not dfs(node, 0):
                    return False
        
        return True