class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])
        answer = []

        for perm in permutations:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                answer.append(perm_copy)
        
        return answer