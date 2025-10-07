class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popped = stack.pop()
                answer[popped[1]] = i - popped[1]
            stack.append((temp, i))
        
        return answer