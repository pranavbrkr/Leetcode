class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hashMap = {}
        answer = 0
        maxFreq = 0

        left = 0
        for right in range(n):
            hashMap[s[right]] = 1 + hashMap.get(s[right], 0)
            maxFreq = max(maxFreq, hashMap[s[right]])

            while ((right - left + 1) - maxFreq) > k:
                hashMap[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer