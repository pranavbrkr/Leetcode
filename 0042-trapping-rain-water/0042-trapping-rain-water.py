class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        max_l = 0
        for i in range(n):
            max_left[i] = max_l
            max_l = max(max_l, height[i])

        max_r = 0
        for i in range(n - 1, -1, -1):
            max_right[i] = max_r
            max_r = max(max_r, height[i])
        
        print(max_left)
        print(max_right)
        
        water = 0
        for i in range(n):
            water_block = min(max_left[i], max_right[i]) - height[i]
            water += water_block if water_block > 0 else 0
        
        return water