class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0

        while n:
            answer += n % 2
            n = n >> 1
        
        return answer