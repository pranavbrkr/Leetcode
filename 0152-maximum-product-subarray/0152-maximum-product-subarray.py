class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        curr_min, curr_max = 1, 1
        
        for number in nums:
            if number == 0:
                curr_min, curr_max = 1, 1
                continue
            temp = curr_max * number
            curr_max = max(number * curr_max, number * curr_min, number)
            curr_min = min(temp, number * curr_min, number)
            answer = max(answer ,curr_max)
        
        return answer