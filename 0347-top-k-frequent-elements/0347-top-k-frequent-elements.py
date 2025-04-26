class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count_num = {}
        for num in nums:
            count_num[num] = 1 + count_num.get(num, 0)

        heap = []
        for num in count_num.keys():
            heapq.heappush(heap, (count_num[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer