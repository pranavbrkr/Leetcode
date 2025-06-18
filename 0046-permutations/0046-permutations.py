class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        freq = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                answer.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    freq[i] = False
            
            return
        
        backtrack([])
        return answer