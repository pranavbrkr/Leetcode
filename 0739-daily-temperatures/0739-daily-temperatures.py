class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i, temp in enumerate(temperatures):
            while len(stack) and stack[-1][0] < temp:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append([temp, i])

        return answer