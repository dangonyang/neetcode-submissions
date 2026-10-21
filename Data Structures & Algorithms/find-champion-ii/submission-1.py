class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker=set(v for u,v in edges)
        candidates=[i for i in range(n) if i not in weaker]
        return candidates[0] if len(candidates)==1 else -1
