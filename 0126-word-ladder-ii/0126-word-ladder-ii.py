class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordList.append(beginWord)
        neighbors = defaultdict(list)

        # Build the pattern-based neighbor map
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbors[pattern].append(word)

        # BFS setup
        q = deque([beginWord])
        visited = set([beginWord])
        found = False
        parents = defaultdict(list)
        level_visited = set()

        while q and not found:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
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

        # If no path found
        if not found:
            return []

        # Backtrack to build all paths
        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        backtrack(endWord, [endWord])
        return res
