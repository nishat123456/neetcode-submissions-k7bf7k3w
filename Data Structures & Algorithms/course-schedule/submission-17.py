class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        #put everything in dict
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set() #to keep track if we visiting it currently and if cycle

        def dfs(crs):
            #we check 2 things. if cycle, if no prereq
            if crs in visiting:
                return False

            if preMap[crs] == []:
                return True
            
            #time to iterate

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): # what does it mean?
                    return False
            visiting.remove(crs)
            preMap[crs] = [] #why? because no cycle?
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True