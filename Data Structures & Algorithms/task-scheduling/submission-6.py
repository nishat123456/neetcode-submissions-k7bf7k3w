class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #n is the cooldown period
        #we make the count of tasks
        #we make max heap and have the freq in it.
        #we make queue to keep track of who is coming when
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque() #pairs of [-cnt, idleTime]
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

