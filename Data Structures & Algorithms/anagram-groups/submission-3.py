class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we use the dict to get the freq of all the letters
        #whenever it is same, we group it. nice
        #i am thinking brute force.

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())