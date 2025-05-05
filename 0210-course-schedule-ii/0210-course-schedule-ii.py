class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        finalized, visited = set(), set()
        output = []

        def dfs(course):
            if course in visited:
                return False
            if course in finalized:
                return True
            
            visited.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            finalized.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output