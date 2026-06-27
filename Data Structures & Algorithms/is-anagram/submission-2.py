class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        #start a dict and we map each letter with their freq
        #if the len of s and t arent same, false
        #elif dict == dict, we true
        if len(s) != len(t):
            return False
        
        freqS = defaultdict(int)
        freqT = defaultdict(int)

        for char in s:
            freqS[char] += 1
        for char in t:
            freqT[char] += 1
        
        if freqS == freqT:
            return True

        return False
        