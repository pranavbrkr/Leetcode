class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        answer = r

        while l <= r:
            k = (l + r) // 2

            total_time = 0
            for p in piles:
                total_time += ceil(p / k)
            
            if total_time <= h:
                answer = min(answer, k)
                r = k - 1
            else:
                l = k + 1

        return answer