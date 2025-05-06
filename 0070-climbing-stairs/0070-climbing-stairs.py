class Solution:
    def climbStairs(self, n: int) -> int:
        down1 = 0
        curr = 1

        for i in range(n):
            temp = curr + down1
            down1 = curr
            curr = temp
        
        return curr