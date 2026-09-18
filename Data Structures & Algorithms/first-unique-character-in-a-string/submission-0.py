class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = defaultdict(int)

        for char in s:
            seen[char] = 1 + seen.get(char, 0)
            print(seen)

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1