class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            target = -nums[i]
            fp = i + 1
            lp = n - 1

            while fp < lp:
                if ((nums[fp] + nums[lp]) == target):
                    answer.append((nums[i], nums[fp], nums[lp]))
                    fp += 1
                    while fp < lp and nums[fp] == nums[fp - 1]:
                        fp += 1
                elif ((nums[fp] + nums[lp]) < target):
                    fp += 1
                else:
                    lp -= 1
            
        return answer