class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while maxHeap:
            if len(maxHeap) == 1:
                return abs(maxHeap[0])

            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            # because x and y are negative, gotta swap
            if x > y:
                heapq.heappush(maxHeap, y - x)
        return 0
