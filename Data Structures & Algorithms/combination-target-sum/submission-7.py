class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtrack
        #dfs, if summ == target: add the copy to res
        #else, if summ > target: return
        #else sum < target, continue

        summ = 0
        res = []
        each = []
        
        def dfs(i, summ):
            if summ == target:
                res.append(each.copy())
                summ = 0
                return

            if summ > target or i == len(nums):
                return

            each.append(nums[i])
            dfs(i, summ + nums[i])

            each.pop()
            dfs(i + 1, summ)

        dfs(0, 0)
        return res

