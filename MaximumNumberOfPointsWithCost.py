# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        max_table = [[0 for _ in range(n)] for _ in range(m)]

        max_table[0] = points[0]

        for i in range(1, m):
            left = [max_table[i - 1][0]]
            right = [max_table[i - 1][-1]]
            for j in range(1, n):
                left.append(max(left[-1] - 1, max_table[i - 1][j]))
            
            for j in range(n - 2, -1, -1):
                right.insert(0, max(right[0] - 1, max_table[i - 1][j]))

            for j in range(n):
                max_table[i][j] = points[i][j] + max(left[j], right[j])

        
        return max(max_table[m - 1])