class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        num_count = dict()

        for number in nums:
            if number in num_count.keys():
                num_count[number] += 1
            else:
                num_count[number] = 1

        num_count_sorted = sorted(num_count.items(), key=lambda x: x[1], reverse = True)

        answer = []
        for i in range(k):
            answer.append(num_count_sorted[i][0])

        return answer
