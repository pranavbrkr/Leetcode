class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [nums[0]]

        for number in nums[1:]:
            answer.append(answer[-1] + number)
        
        return answer