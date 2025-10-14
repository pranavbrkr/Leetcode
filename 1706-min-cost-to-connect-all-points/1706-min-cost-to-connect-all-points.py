class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        
        edges.sort()

        min_cost = 0
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            res = node
            while res != parent[res]:
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
            
            rank[p1] += rank[p2]
            parent[p2] = p1
            return True
        
        for cost, i, j in edges:
            if union(i, j):
                min_cost += cost
        
        return min_cost