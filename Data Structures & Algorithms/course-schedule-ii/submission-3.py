class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        
        #do the map
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        visiting = set()
        completed = set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in completed:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            completed.add(crs)
            res.append(crs)
            return True


        #iterate
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res