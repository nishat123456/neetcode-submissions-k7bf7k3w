class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        each = []

        def backtracking(i):

            if len(each) == k:
                res.append(each.copy())
                return
            
            if i > n:
                return

            each.append(i)
            backtracking(i + 1)

            each.pop()
            backtracking(i + 1)

        backtracking(1)
        return res
            
