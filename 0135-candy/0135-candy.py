class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = 1
        i = 1

        while i < n:
            if ratings[i] == ratings[i - 1]:
                candies += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                candies += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                candies += down
                down += 1
                i += 1
            
            if down > peak:
                candies += (down - peak)

        return candies