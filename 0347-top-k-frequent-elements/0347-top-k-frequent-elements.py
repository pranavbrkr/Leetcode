class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_nums = defaultdict(int)
        for num in nums:
            count_nums[num] += 1

        heap = []
        for number in count_nums.keys():
            heapq.heappush(heap, (count_nums[number], number))
            if len(heap) > k:
                heapq.heappop(heap)

        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer