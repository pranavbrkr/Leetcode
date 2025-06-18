class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                answer.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()
            while (i + 1) < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)
            return
        
        backtrack(0, [])
        return answer