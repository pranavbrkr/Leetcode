class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list1 = s1.split(' ')
        list2 = s2.split(' ')

        hash1 = {}
        hash2 = {}

        for word in list1:
            if word not in hash1.keys():
                hash1[word] = 1
            else:
                hash1[word] += 1

        for word in list2:
            if word not in hash2.keys():
                hash2[word] = 1
            else:
                hash2[word] += 1
        
        answer = []

        for word, count in hash1.items():
            if count == 1 and word not in hash2.keys():
                answer.append(word)

        for word, count in hash2.items():
            if count == 1 and word not in hash1.keys():
                answer.append(word)

        return answer