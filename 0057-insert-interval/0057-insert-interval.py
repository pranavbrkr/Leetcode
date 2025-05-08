class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        answer = []

        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                answer.append(newInterval)
                return answer + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                answer.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        answer.append(newInterval)
        return answer