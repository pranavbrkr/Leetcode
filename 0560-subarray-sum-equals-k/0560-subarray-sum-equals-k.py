class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = {0: 1}
        curr_sum = 0

        for number in nums:
            curr_sum += number
            answer += prefix_sum.get(curr_sum - k, 0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)

        
        return answer

        # n = len(nums)
        # answer = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for ln in range(n):
        #             if (j + ln < n):
        #                 if sum(nums[i:j + ln]) == k:
        #                     print(i, j + ln)
        #                     print(nums[i:j + ln])
        #                     answer += 1
        #                     continue
        # return answer





#  1,2,3

# 0: 1
# 1: 1
# 3: 1
