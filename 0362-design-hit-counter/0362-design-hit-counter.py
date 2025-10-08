class HitCounter:

    def __init__(self):
        self.hits = []
        self.total_hits = 0

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.total_hits += 1
        

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300

        left, right = 0, self.total_hits - 1

        while left <= right:
            mid = (left + right) // 2

            if self.hits[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return self.total_hits - left


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)