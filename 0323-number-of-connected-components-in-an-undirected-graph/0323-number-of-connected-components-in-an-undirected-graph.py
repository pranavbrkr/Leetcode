class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        num_components = 0
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for i in adj:
            if i not in visited:
                visited.add(i)
                num_components += 1
                dfs(i)
        
        return num_components