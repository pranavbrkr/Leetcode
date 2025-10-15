class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        dp = {}

        def partition(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            max_coins = float('-inf')
            for index in range(i, j + 1):
                cost = nums[i - 1] * nums[index] * nums[j + 1] + partition(i, index - 1) + partition(index + 1, j)
                max_coins = max(max_coins, cost)
            
            dp[(i, j)] = max_coins
            return dp[(i, j)]
        
        return partition(1, n)