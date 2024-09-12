class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        set_allowed = set(allowed)

        for word in words:
            set_word = set(word)

            if set_word <= set_allowed:
                answer += 1
        
        return answer