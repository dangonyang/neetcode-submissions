class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adjacency list
        adjList = {}
        for src, dst in edges:
            if src not in adjList:
                adjList[src] = []
            adjList[src].append(dst)

        # top sort result
        topSort = []
        visited = set()
        visiting = set()
        # visit set
        # currently visiting set

        # dfs helper function
        def dfs(src: int) -> bool:
            if src in visited:
                return True
            if src in visiting:
                # cycle
                return False

            visiting.add(src)
            for neighbor in adjList.get(src, []):
                if not dfs(neighbor):
                    # cycle
                    return False
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                # cycle detected
                return []
        
        topSort.reverse()
        return topSort

