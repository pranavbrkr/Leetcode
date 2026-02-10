class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_arr = [1] * n
        postfix_arr = [1] * n

        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix_arr[i] = postfix_arr[i + 1] * nums[i + 1]
        

        answer = []
        for i in range(len(nums)):
            answer.append(prefix_arr[i] * postfix_arr[i])
        return answer