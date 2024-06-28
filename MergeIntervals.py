# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        answer = []
        n = len(intervals)

        i = 0
        currStart = intervals[i][0]
        currEnd = intervals[i][1]
        i += 1

        while i < n:
            if currEnd >= intervals[i][0] or currEnd >= intervals[i][1]:
                currStart = min(currStart, intervals[i][0])
                currEnd = max(currEnd, intervals[i][1])
            else:
                answer.append([currStart, currEnd])
                currStart = intervals[i][0]
                currEnd = intervals[i][1]
            i += 1
        
        answer.append([currStart, currEnd])
        return answer