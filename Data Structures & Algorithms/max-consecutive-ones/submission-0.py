class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ones = 0
        maxO = 0
        if not nums:
            return 0

        for l in range(len(nums)):
            if nums[l] == 1:
                ones += 1
                maxO = max(ones, maxO)
                continue

            if nums[l] == 0:
                ones = 0

        return maxO