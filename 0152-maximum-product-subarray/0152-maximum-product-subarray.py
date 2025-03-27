class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        curr_max, curr_min = 1, 1

        for number in nums:
            if number == 0:
                curr_max, curr_min = 1, 1
                continue
            
            temp = curr_max * number
            curr_max = max(curr_max * number, curr_min * number, number)
            curr_min = min(temp, curr_min * number, number)
            answer = max(answer, curr_max)
        
        return answer