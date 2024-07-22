# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        first, last = 0, n - 1
        max_volume = float('-inf')

        while last > first:
            current_volume = (last - first) * min(height[first], height[last])
            max_volume = current_volume if current_volume >= max_volume else max_volume

            if height[last] <= height[first]:
                last -= 1
            else:
                first += 1

        return max_volume