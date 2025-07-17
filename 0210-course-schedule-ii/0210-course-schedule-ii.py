class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for sub, dep in prerequisites:
            graph[sub].append(dep)
            indegree[dep] += 1

        order = []
        queue = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] <= 0:
                    queue.append(nei)
        
        return order[::-1] if len(order) == numCourses else []