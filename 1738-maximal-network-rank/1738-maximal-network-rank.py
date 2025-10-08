class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)

        for c1, c2 in roads:
            graph[c1].add(c2)
            graph[c2].add(c1)

        max_rank = 0        
        for city1 in range(n):
            for city2 in range(city1 + 1, n):

                current_rank = len(graph[city1]) + len(graph[city2])
                if city2 in graph[city1]:
                    current_rank -= 1
                
                max_rank = max(max_rank, current_rank)
        

        return max_rank