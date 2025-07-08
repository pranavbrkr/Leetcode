class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        answer = 0

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                answer += 1
                prev_end = min(prev_end, end)
        
        return answer