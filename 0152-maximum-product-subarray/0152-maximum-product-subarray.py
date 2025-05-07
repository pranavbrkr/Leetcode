class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        curr_max, curr_min = 1, 1

        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue
            
            temp = curr_max * n
            curr_max = max(temp, curr_min * n, n)
            curr_min = min(temp, curr_min * n, n)
            answer = max(answer, curr_max)
        
        return answer