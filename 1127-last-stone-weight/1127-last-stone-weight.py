class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-stone for stone in stones]
        heapq.heapify(arr)
        while len(arr) > 1:
            y = -heapq.heappop(arr)
            x = -heapq.heappop(arr)
            if x != y:
                heapq.heappush(arr, -(y - x))
        return -arr[0] if arr else 0