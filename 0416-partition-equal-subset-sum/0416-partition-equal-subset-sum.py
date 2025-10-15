class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for number in nums:
            next_dp = set()
            for t in dp:
                next_dp.add(t + number)
                next_dp.add(t)
            dp = next_dp
        
        return True if target in dp else False