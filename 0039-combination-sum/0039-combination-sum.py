class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(index, subarray, total):
            if total == target:
                answer.append(subarray.copy())
                return
            
            if index >= len(candidates):
                return
            
            if total > target:
                return
            
            for j in range(index, len(candidates)):
                subarray.append(candidates[j])
                backtrack(j, subarray, total + candidates[j])
                subarray.pop()
        
        backtrack(0, [], 0)
        return answer