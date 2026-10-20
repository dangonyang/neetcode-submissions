class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque([src])
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            for neighbor in self.adjList.get(curr, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            visited.add(curr)
        return False
                

