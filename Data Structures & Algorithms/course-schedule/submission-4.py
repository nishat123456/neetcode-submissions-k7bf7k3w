class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #what are graphs made of? - list
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

            #visitset = all courses along curr DFS

        visitSet = set()
        def dfs(crs):
            if crs in visitSet: #loop
                return False
            
            if preMap[crs] == []: #empty
                return True

            visitSet.add(crs) #starts the DFS path
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True