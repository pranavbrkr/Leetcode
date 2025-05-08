class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        answer = []
        n = len(intervals)

        for i in range(n):
            if answer and answer[-1][1] >= intervals[i][0]:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])
            else:
                answer.append(intervals[i])
        
        return answer