class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)

        for c1, c2 in roads:
            graph[c1].add(c2)
            graph[c2].add(c1)

        max_rank = 0        
        for city1 in graph.keys():
            for city2 in graph.keys():
                if city1 == city2:
                    continue
                
                if max_rank < (len(graph[city1]) + len(graph[city2])):
                    max_rank = (len(graph[city1]) + len(graph[city2]))
                    max_rank += -1 if city2 in graph[city1] else 0
        

        return max_rank