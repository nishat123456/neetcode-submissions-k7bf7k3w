class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)

        l = 0
        score = 0
        minS = 9999
        for r in range(len(nums)):
            if (r - l + 1) == k:
                score = nums[r] - nums[l]
                minS = min(minS, score)
                print(minS)

                l += 1
        return minS
