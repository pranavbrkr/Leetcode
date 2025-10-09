class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        hash_set = set(nums)

        for i in range(1, n + 1):
            if i not in hash_set:
                return i
        
        return n + 1