class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            
            return True
        
        answer = []
        partition = []
        def backtrack(i):
            if i >= len(s):
                answer.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    partition.append(s[i : j + 1])
                    backtrack(j + 1)
                    partition.pop()
            
            return
        
        backtrack(0)
        return answer