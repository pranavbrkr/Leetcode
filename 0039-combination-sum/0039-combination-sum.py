class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, curr, total):
            if total == target:
                answer.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            curr.pop()
            dfs(i + 1, curr, total)

            return
        
        dfs(0, [], 0)
        return answer