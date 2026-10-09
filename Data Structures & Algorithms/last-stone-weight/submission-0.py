class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # input: int list
        # output: int

        # goal: smash all pairs of heavy stones until you can't anymore
        # method: use a heap and pop two at a time
        
        # heapify stones -> biggest at top
        # pop two at a time, input new
        # return last remaining stone

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            # x and y are negative, so need to reverse sign
            if y > x:
                heapq.heappush(heap, x - y)
            
        if heap:
            return abs(heap[0])
        return 0