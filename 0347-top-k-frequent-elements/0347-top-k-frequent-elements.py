class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        
        heap = []

        for number in count.keys():
            heapq.heappush(heap, (count[number], number))
            if len(heap) > k:
                heapq.heappop(heap)
        
        answer = []
        while k:
            answer.append(heapq.heappop(heap)[1])
            k -= 1
        
        return answer