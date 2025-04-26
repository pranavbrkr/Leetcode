class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}

        for i, number in enumerate(nums):
            if (target - number) in num_set:
                return [i, num_set[target - number]]
            num_set[number] = i