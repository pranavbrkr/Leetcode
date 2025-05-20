class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(max_heap)

        prev = None
        answer = ""

        while prev or max_heap:
            if not max_heap and prev:
                return ""
            cnt, char = heapq.heappop(max_heap)
            answer += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return answer