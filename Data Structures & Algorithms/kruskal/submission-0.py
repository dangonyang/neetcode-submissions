class UnionFind:

    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, n1: int, n2: int) -> bool:
        root_x = self.find(n1)
        root_y = self.find(n2)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
        else:
            self.par[root_y] = root_x
            self.rank[root_x] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # initialize minHeap (choosing smallest value)
        minHeap = []
        # iterate through all edges
        for n1, n2, weight in edges:
            # push edges into heap
            heapq.heappush(minHeap, [weight, n1, n2])
        
        # union find n to keep track of connected components
        unionFind = UnionFind(n)
        length = 0
        nodes = n

        # pop edges from in heap and connect the nodes
        while minHeap and nodes > 1:
            weight, n1, n2 = heapq.heappop(minHeap)
            if unionFind.union(n1, n2):
                length += weight
                nodes -= 1
        return length if nodes == 1 else -1
