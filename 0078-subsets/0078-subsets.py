class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def backtrack(index):
            if index >= len(nums):
                answer.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()
            backtrack(index + 1)
            return
        
        backtrack(0)
        return answer