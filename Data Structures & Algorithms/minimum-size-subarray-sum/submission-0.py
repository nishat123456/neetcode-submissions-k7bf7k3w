class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #nums
        #target
        #return len(min_subarray)
        # sum_subarray >= target
        #else 0

        left = 0
        min_len = float('inf')
        summ = 0
        
        for right in range(len(nums)):
            summ += nums[right]
            
            while summ >= target:
                min_len = min(min_len, right - left + 1)
                summ -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0

        else:
            return min_len      
