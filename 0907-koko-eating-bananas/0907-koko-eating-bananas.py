class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right

        while left <= right:
            k = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / k)

            if total_hours <= h:
                answer = min(answer, k)
                right = k - 1
            else:
                left = k + 1

        return answer