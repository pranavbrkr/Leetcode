class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        left_max = right_max = water = 0

        while l < r:
            if height[l] <= height[r]:
                if left_max > height[l]:
                    water += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if right_max > height[r]:
                    water += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1
        
        return water