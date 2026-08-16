class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def rob_c(nums):
            memo = [-1] * len(nums)

            def dfs(i):
                n = len(nums)
                

                if i >= n:
                    return 0

                if memo[i] != -1:
                    return memo[i]

                memo[i] = max(dfs(i + 1), nums[i] + dfs(i+2))
                return memo[i]

            return dfs(0)

        if len(nums) == 1:
            return nums[0]

        return max(rob_c(nums[1:]), rob_c(nums[:-1]))
        