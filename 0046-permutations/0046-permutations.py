class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = [[]]

        for number in nums:
            new_perms = []
            for perm in answer:
                for i in range(len(perm) + 1):
                    p_copy = perm.copy()
                    p_copy.insert(i, number)
                    new_perms.append(p_copy)
            answer = new_perms
        
        return answer