class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0 or n == 1:
            return 0

        left, right = 0, n - 1
        max_left, max_right = height[left], height[right]

        left += 1
        right -= 1

        water = 0

        while left <= right:
            if max_left <= max_right:
                if max_left - height[left] > 0:
                    water += max_left - height[left]
                    print(f"Water {water} at left {left}")
            else:
                if max_right - height[right] > 0:
                    water += max_right - height[right]
                    print(f"Water {water} at right {right}")

            if max_left <= max_right:
                if max_left < height[left]:
                    max_left = height[left]
                left += 1
            else:
                if max_right < height[right]:
                    max_right = height[right]
                right -= 1
            
            print(f"l: {left}, r: {right}")

        return water