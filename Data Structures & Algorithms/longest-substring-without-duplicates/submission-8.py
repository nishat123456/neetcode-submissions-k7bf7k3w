class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #r goes all the way
        #if not duplicate, add to window
        #update longest
        #while duplicate, move l 
        #return longest

        #set

        l = 0
        seen = set()
        longest = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest