class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for key in count:
            minHeap.append((-count[key], key))
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            num_count, num = heapq.heappop(minHeap)
            res.append(num)
        return res