class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer, count = 0, 0

        for number in nums:
            if count == 0:
                answer = number
            count += (1 if answer == number else -1)
        
        return answer