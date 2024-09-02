class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        chalk_sum = sum(chalk)

        rem_chalk = k % chalk_sum

        i = 0

        while chalk[i] <= rem_chalk:
            rem_chalk -= chalk[i]
            i += 1

        return i