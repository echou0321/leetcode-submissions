class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        heapq.heapify_max(maxheap)

        while len(maxheap) > 1:
            first = heapq.heappop_max(maxheap)
            second = heapq.heappop_max(maxheap)

            if first != second:
                new = first - second
                heapq.heappush_max(maxheap, new)
        
        return heapq.heappop_max(maxheap) if maxheap else 0
