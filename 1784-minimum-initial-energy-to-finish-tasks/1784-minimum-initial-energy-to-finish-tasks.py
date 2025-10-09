class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)

        answer = 0
        curr_energy = 0

        for cost, req in tasks:
            if req > curr_energy:
                answer += (req - curr_energy)
                curr_energy = req
            curr_energy -= cost
        
        return answer