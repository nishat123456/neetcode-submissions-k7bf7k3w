class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we use the dict to get the freq of all the letters
        #whenever it is same, we group it. nice
        #i am thinking brute force.

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())