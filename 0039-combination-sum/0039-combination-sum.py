class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(i, path, total):
            if total == target:
                answer.append(path.copy())
                return
            if total>target:
                return
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                backtrack(j, path, total + candidates[j])
                path.pop()

        backtrack(0, [], 0)
        return answer