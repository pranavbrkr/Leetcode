class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        n = len(height)

        max_height = 0
        for i in range(n):
            max_left.append(max_height)
            max_height = max(max_height, height[i])

        max_height = 0
        for i in range(n - 1, -1, -1):
            max_right.append(max_height)
            max_height = max(max_height, height[i])
        max_right.reverse()

        print(max_left)
        print(max_right)


        water = 0
        for i in range(n):
            if (min(max_left[i], max_right[i]) - height[i]) > 0:
                water += min(max_left[i], max_right[i]) - height[i]
        
        return water