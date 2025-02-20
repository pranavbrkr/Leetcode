class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        n = len(nums)
        
        for i, number in enumerate(nums):
            rem = target - number
            if rem in num_set:
                return [i, num_set[rem]]
            num_set[number] = i
        
        return