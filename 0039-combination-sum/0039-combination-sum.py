class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(index, subarray, total):
            if total == target:
                answer.append(subarray.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            subarray.append(candidates[index])
            backtrack(index, subarray, total + candidates[index])
            subarray.pop()
            backtrack(index + 1, subarray, total)
        
        backtrack(0, [], 0)
        return answer