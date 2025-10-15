class Solution:
    def climbStairs(self, n: int) -> int:
        down2 = 1
        down1 = 1

        for i in range(n - 1):
            temp = down2 + down1
            down2 = down1
            down1 = temp

        return down1