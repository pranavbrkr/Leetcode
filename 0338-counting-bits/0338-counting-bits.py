class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            answer[i] = 1 + answer[i - offset]

        return answer