class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for number in nums:
            counter[number] += 1

        heap = []

        for number in counter.keys():
            heapq.heappush(heap, (counter[number], number))
            if len(heap) > k:
                heapq.heappop(heap)
        
        answer = []
        while len(heap):
            answer.append(heapq.heappop(heap)[1])
        
        return answer