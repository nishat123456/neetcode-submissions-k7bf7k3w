class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we do backtrack with dfs(i, summ)
        #if summ == target, append to res.
        #if summ > target or i == len(nums): return
        #each.append(nums[i])
        #dfs(i + 1, summ+ nums[i])
        #each.pop()
        #dfs(i + 1, summ)
        res = []
        each = []

        candidates.sort()
        
        
        def dfs(i, summ):
            if summ == target:
                res.append(each.copy())
                return

            if summ > target or i == len(candidates):
                return

            each.append(candidates[i])
            
            dfs(i + 1, summ + candidates[i])

            each.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, summ)

        dfs(0, 0)
        return res