class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = [[] for _ in range(numCourses)]

        for sub, dep in prerequisites:
            course_graph[sub].append(dep)
        
        visited = [False] * numCourses
        path_visited = [False] * numCourses

        def dfs(course):
            visited[course] = True
            path_visited[course] = True

            for dep in course_graph[course]:
                if not visited[dep]:
                    if not dfs(dep):
                        return False
                elif path_visited[dep]:
                    return False
            
            path_visited[course] = False
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        
        return True