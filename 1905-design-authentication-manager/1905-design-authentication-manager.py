class Node:
    def __init__(self, tokenId, ttl = -1):
        self.token_id, self.ttl = tokenId, ttl
        self.next, self.prev = None, None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.cache = {}
        self.time_to_live = timeToLive
        self.size = 0
        self.right, self.left = Node(-1), Node(-1)
        self.right.prev, self.left.next = self.left, self.right
    
    def insert(self, node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.cache:
            self.remove(self.cache[tokenId])
            self.size -= 1
        self.cache[tokenId] = Node(tokenId, currentTime + self.time_to_live)
        self.insert(self.cache[tokenId])
        self.size += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        node = self.cache.get(tokenId, None)
        if node and node.ttl > currentTime:
            self.remove(node)
            self.cache[tokenId] = Node(tokenId, currentTime + self.time_to_live)
            self.insert(self.cache[tokenId])

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.left.next is not self.right and self.left.next.ttl <= currentTime:
            expired_node = self.left.next
            self.remove(expired_node)
            del self.cache[expired_node.token_id]
            self.size -= 1
        
        return self.size

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)