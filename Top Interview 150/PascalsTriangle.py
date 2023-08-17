# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        output = []

        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    row.append(output[i-1][j] + output[i-1][j-1])
            output.append(row)
            
        return output