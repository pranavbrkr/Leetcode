class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def backtrack(i, curr, total):
            if total == target:
                answer.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            # Include candidate[i]
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])

            # Skip candidate[i]
            curr.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr, total)
            return
        
        backtrack(0, [], 0)
        return answer