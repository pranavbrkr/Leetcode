class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        missing = 1
        for number in nums:
            if missing == number:
                missing += 1
        
        return missing