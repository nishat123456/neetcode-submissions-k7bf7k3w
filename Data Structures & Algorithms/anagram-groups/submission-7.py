class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each word, make the key of a dict that does the fingerprint part, use tuple cz immutable.
        #we match the key, then append.
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1 #making the key here, ASCII values
            res[tuple(count)].append(s)

        return list(res.values())


        