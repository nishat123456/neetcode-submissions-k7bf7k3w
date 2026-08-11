class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        if len(s) != len(t):
            return False

        for char in s:
            hmap[char] = 1 + hmap.get(char, 0)

        for char in t:
            if char not in hmap:
                return False

            hmap[char] -= 1

            if hmap[char] < 0:
                return False

        return True