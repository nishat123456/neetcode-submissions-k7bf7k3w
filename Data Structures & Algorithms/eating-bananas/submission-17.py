class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l < r:
            k = l + (r - l)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)

            if hours > h:
                l = k + 1
            else:
                r = k
        return l 


        

