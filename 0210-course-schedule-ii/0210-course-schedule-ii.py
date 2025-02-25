class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = { c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            pre_req[crs].append(pre)
        
        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in pre_req[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output