class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(index):
            if index == len(nums):
                answer.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
            
            return
        
        backtrack(0)
        return answer