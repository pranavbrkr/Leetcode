class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for start in range(n):
            if color[start] == -1:
                queue = deque()
                queue.append(start)
                color[start] = 0
                while queue:
                    node = queue.popleft()
                    for adj in graph[node]:
                        if color[adj] == -1:
                            color[adj] = not color[node]
                            queue.append(adj)
                            print(queue)
                        elif color[adj] == color[node]:
                            return False
                
        return True