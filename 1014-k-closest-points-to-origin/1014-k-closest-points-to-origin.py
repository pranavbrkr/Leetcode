class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidean(x1, y1):
            return (x1 * x1 + y1 * y1) ** 0.5
        

        heap = []
        heapq.heapify(heap)

        for point in points:
            heapq.heappush(heap, (euclidean(point[0], point[1]), point))
        
        answer = []

        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer