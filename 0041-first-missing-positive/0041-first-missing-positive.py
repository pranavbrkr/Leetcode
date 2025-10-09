class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash = set()
        max_num = 0

        for number in nums:
            if number > 0:
                hash.add(number)
                max_num = max(max_num, number)
        
        for i in range(1, max_num + 1):
            if i not in hash:
                return i
        
        return max_num + 1