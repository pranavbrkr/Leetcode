class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        for n in nums:
            new_perm = []
            for perm in answer:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, n)
                    new_perm.append(perm_copy)
            answer = new_perm
        return answer