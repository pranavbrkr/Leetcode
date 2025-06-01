class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        curr_sum = 0
        prefix = { 0: 1}

        for number in nums:
            curr_sum += number
            diff = curr_sum - k
            answer += prefix.get(diff, 0)
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)

        return answer