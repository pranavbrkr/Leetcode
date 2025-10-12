class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def backtrack(index, subarr, total):
            if total == target:
                answer.append(subarr.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            subarr.append(candidates[index])
            backtrack(index + 1, subarr, total + candidates[index])

            subarr.pop()
            while (index + 1) < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, subarr, total)

            return
        
        backtrack(0, [], 0)
        return answer