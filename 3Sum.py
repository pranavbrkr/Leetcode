# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []

        nums = sorted(nums)
        n = len(nums)


        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            target = -nums[i]
            fp = i + 1
            lp = n - 1

            while fp < lp:
                if ((nums[fp] + nums[lp]) == target):
                    answer.append([nums[i], nums[fp], nums[lp]])
                    fp += 1
                    while nums[fp] == nums[fp - 1] and fp < lp:
                        fp += 1
                elif ((nums[fp] + nums[lp]) > target):
                    lp -= 1
                else:
                    fp += 1

        return answer