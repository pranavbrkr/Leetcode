class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.total_hits = 0

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            self.hits.append((timestamp, 1))
        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and (timestamp - self.hits[0][0]) >= 300:
            self.total_hits -= self.hits[0][1]
            self.hits.popleft()
        
        return self.total_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)