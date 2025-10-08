class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.total_hits = 0

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and (timestamp - self.hits[0]) >= 300:
            self.hits.popleft()
            self.total_hits -= 1
        
        return self.total_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)