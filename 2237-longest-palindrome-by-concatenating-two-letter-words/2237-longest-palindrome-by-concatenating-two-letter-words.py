class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        answer = 0
        central = False

        for w, w_count in word_count.items():
            if w[0] == w[1]:
                if w_count % 2 == 0:
                    answer += w_count
                else:
                    answer += w_count - 1
                    central = True
            elif w[0] < w[1]:
                answer += 2 * min(w_count, word_count[w[1] + w[0]])
        
        if central:
            answer += 1
        return 2 * answer