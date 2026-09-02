class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #first we take the highest we can eat. Max(piles)
        #then we keep going binary search and see if we can still finish in time.
        r = max(piles)
        l = 1

        while l < r:
            k = l + (r - l) //2 #bananas per hour
            
            hours = 0
            for pile in piles: #instead of chaning one by one, we change by each value.
                hours += math.ceil(pile/k) #we want to get how many hours we need to finish it

            if hours > h:
                l = k + 1
            else:
                r = k

        return l

