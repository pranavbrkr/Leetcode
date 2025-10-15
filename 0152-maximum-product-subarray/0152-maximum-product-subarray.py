class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            temp = n * curr_max
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(temp, n * curr_min, n)
            answer = max(answer, curr_max)
        
        return answer