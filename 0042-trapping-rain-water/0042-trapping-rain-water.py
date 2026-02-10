class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = max_right = water = 0
        l, r = 0, n - 1

        while l < r:
            if height[l] <= height[r]:
                if max_left > height[l]:
                    water += max_left - height[l]
                else:
                    max_left = height[l]
                l += 1
            else:
                if max_right > height[r]:
                    water += max_right - height[r]
                else:
                    max_right = height[r]
                r -= 1

        return water