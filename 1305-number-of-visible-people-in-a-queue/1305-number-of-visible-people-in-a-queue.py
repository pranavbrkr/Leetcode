class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            visible = 0
            while stack and heights[i] > stack[-1]:
                visible += 1
                stack.pop()
            
            if stack:
                visible += 1
            
            answer[i] = visible
            stack.append(heights[i])
    
        return answer