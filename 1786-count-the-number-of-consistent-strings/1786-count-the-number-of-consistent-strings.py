class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = len(words)
        mask = 0

        for char in allowed:
            bit = 1 << (ord(char) - ord('a'))
            mask = mask | bit
        
        for word in words:
            for char in word:
                bit = 1 << (ord(char) - ord('a'))
                if bit & mask == 0:
                    answer -= 1
                    break
        
        return answer