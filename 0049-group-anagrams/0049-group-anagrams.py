class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            counter = [0] * 26

            for char in s:
                counter[ord(char) - ord('a')] += 1

            answer[tuple(counter)].append(s)
        
        return list(answer.values())