class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(index, subarr, total):
            if total == target:
                answer.append(subarr.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            subarr.append(candidates[index])
            backtrack(index, subarr, total + candidates[index])

            subarr.pop()
            backtrack(index + 1, subarr, total)

            return
        
        backtrack(0, [], 0)
        return answer