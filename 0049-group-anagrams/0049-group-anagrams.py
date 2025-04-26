class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            counter = [0] * 26

            for s in string:
                counter[ord(s) - ord('a')] += 1
            
            groups[tuple(counter)].append(string)
        
        return list(groups.values())