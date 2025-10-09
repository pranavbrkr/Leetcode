class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0] - x[1])

        answer = 0
        curr = 0

        for cost, mini in tasks:
            if mini > curr:
                answer += (mini - curr)
                curr = mini
            curr -= cost
        
        return answer