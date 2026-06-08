class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)
        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        
        return time