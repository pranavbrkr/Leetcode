class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i : [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True

            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True