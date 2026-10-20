class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # create adjacency list
        adjList = {}
        for start, dst, weight in edges:
            if start not in adjList:
                adjList[start] = []
            adjList[start].append((dst, weight))
        # create shortest hm
        shortest = {}
        # create minHeap with elements in form of (weight, node)
        minHeap = [(0, src)]
        # while minHeap
        while minHeap:
            # pop from heap -> weight, node
            weight, node = heapq.heappop(minHeap)
            # if shortest path already found
            if node in shortest:
                # continue
                continue
            # shortest path is this path
            shortest[node] = weight
            # for each neighbor of the node
            for neighbor, n_weight in adjList.get(node, []):
                # append (min weight, neighbor)
                heapq.heappush(minHeap, (n_weight + weight, neighbor))
        # fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        # return shortest if it exists else -1
        return shortest
                