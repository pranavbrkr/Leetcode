class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                answer.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # do not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return answer