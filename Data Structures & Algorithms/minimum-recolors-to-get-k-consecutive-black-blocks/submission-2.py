class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #i need a window where (r - l + 1) == k
        #while r goes, r counts W.
        #then if windows goes out of bound, l forwards, if finds W, w -= 1
        #we keep count of min W in the window.

        l = 0
        r = l
        w = 0
        minW = 99999999
        while r < len(blocks):
            if blocks[r] == 'W':
                w += 1
            window = (r - l + 1)

            if window == k:
                minW = min(w, minW)

                if blocks[l] == 'W':
                    w -= 1
                l += 1
            r += 1
            
        return minW
                

            