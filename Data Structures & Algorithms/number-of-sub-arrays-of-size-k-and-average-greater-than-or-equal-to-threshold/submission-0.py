class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        sumA = 0
        numO = 0
        for r in range(len(arr)):
            sumA += arr[r]
            if (r - l + 1) == k:
                avgA = sumA / k
                if avgA >= threshold:
                    numO += 1
                sumA -= arr[l]

                l += 1
        return numO
        

                
            
            