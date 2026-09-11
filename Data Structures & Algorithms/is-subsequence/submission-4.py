class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #we we go one letter by one letter.
        #one pointer goes from s, one from t. T moves on as long as it doesn't find the char in s. we could use queue and do popleft. Think this is optimized. What is the brute force one?
        l = 0
        for r in range(len(t)):
            if s and t[r] == s[l]:
                l += 1

            if l == (len(s)):
                return True
            
        return False
