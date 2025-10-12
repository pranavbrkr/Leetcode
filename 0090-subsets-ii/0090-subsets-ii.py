class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        def backtrack(index, subarr):
            if index >= len(nums):
                answer.append(subarr.copy())
                return
            
            subarr.append(nums[index])
            backtrack(index + 1, subarr)

            subarr.pop()
            while (index + 1) < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, subarr)

            return
        
        backtrack(0, [])
        return answer