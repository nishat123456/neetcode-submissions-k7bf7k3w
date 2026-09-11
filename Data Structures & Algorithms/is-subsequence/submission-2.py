class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #we we go one letter by one letter.
        #one pointer goes from s, one from t. T moves on as long as it doesn't find the char in s. we could use queue and do popleft. Think this is optimized. What is the brute force one?
        queue = deque(s)
        if not s:
            return True

        for char in t:
            if queue and char in queue[0]:
                queue.popleft()
                print(queue)

        return True if not queue else False
