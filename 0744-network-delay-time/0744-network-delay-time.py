class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        heap = [(0, k)]
        visited = set()

        time = 0

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            time = max(time, w1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w1 + w2, n2))
        
        return time if len(visited) == n else -1