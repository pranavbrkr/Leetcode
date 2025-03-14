class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_volume = float("-inf")

        while l < r:
            curr_volume = (r - l) * min(height[l], height[r])
            max_volume = max(max_volume, curr_volume)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return max_volume