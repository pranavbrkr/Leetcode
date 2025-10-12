class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        m, n = len(board), len(board[0])
        visited, answer = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word:
                answer.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return list(answer)