class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        n = len(intervals)
        s, e = 0, 0
        answer, count = 0, 0

        while s < n:
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            answer = max(answer, count)
        
        return answer