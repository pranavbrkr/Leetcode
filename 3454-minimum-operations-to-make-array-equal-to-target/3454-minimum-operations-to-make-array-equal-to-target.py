class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diff = [nums[i] - target[i] for i in range(n)]
        min_ops = abs(diff[0])

        for i in range(1, n):
            if diff[i] >= 0 and diff[i - 1] >= 0:
                min_ops += max(diff[i] - diff[i - 1], 0)
            elif diff[i] <= 0 and diff[i - 1] <= 0:
                min_ops += max(abs(diff[i]) - abs(diff[i - 1]), 0)
            else:
                min_ops += abs(diff[i])
        
        return min_ops