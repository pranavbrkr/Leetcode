# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        answer = []
        
        n = len(intervals)
        i = 0

        while i < n:
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            else:
                i += 1

        if n == len(intervals):
            intervals.append(newInterval)


        answer = []
        i = 0

        for interval in intervals:
            if not len(answer):
                answer.append(interval)
                continue

            if interval[0] <= answer[i][1]:
                answer[i][1] = max(answer[i][1], interval[1])
            else:
                answer.append(interval)
                i += 1

        return answer