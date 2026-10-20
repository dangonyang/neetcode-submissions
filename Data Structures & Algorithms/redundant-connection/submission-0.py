class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            # finds root of x
            # if current node is not the parent node
            if n != par[n]:
                # make parent of node = to root parent
                par[n] = find(par[n])
            return par[n]
        
        # sees if nodes dont have cycle
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # shares parent, can't union
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        

        
        