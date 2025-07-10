class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
        
        right = [1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right.insert(0, right[0] + 1)
            else:
                right.insert(0, 1)
        
        return sum([max(left[i], right[i]) for i in range(n)])