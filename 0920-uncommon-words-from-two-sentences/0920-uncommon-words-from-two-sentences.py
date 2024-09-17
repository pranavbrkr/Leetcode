class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hash_map = defaultdict(int)

        for word in s1.split(' ') + s2.split(' '):
            hash_map[word] += 1
        
        answer = []

        for word, count in hash_map.items():
            if count == 1:
                answer.append(word)

        return answer