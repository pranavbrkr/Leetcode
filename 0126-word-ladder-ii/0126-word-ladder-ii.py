class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordList.append(beginWord)
        neighbors = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbors[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        found = False
        level_visited = set()
        parents = defaultdict(list)

        while q and not found:
            for _ in range(len(q)):
                word = q.popleft()
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in neighbors[pattern]:
                        if nei not in visited:
                            if nei == endWord:
                                found = True
                            if nei not in level_visited:
                                level_visited.add(nei)
                                q.append(nei)
                            parents[nei].append(word)
            visited.update(level_visited)
            level_visited.clear()
        
        if not found:
            return []
        
        answer = []

        def backtrack(word, path):
            if word == beginWord:
                answer.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])
        
        backtrack(endWord, [endWord])
        return answer