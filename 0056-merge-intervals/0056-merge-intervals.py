class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        answer = []

        for interval in intervals:
            if answer and interval[0] <= answer[-1][1]:
                answer[-1][1] = max(interval[1], answer[-1][1])
            else:
                answer.append(interval)
        
        return answer