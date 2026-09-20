class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        each = []

        def dfs(i):
            if i == len(nums):
                res.append(each.copy())

                return

            each.append(nums[i])
            dfs(i + 1)
            each.pop()
            
            dfs(i + 1)

        dfs(0)
        return res