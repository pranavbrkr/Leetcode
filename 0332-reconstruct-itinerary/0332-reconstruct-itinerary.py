class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        itinerary = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            itinerary.append(src)
        
        dfs("JFK")
        return itinerary[::-1]