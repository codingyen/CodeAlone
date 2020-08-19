from collections import defaultdict

class Solution:
    def countComponents(self, n, edge):
        res = n
        roots = [-1] * n
        for u , v in edges:
            t1 = self.find(roots, u)
            t2 = self.find(roots, v)
            if t1 != t2:
                roots[t2] = t1
                res -= 1
        return res
    
    def find(self, roots, u):
        if roots[u] == -1:
            return u
        else:
            roots[u] = self.find(roots, roots[u])
            return roots[u]
        #while(roots[u] != -1):
        #    u = roots[u]
        #return u

"""
# Solution 1
    def countComponents(self, n, edge):
        self.parent = {item : item for item in range(n)}
        self.group = defaultdict(list)

        for u, v in edges:
            self.union(u, v)

        for i in range(n):
            self.group[self.parent[i]].append(i)

        return len(self.group)

    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

    def union(self, u, v):
        t1 = self.find(u)
        t2 = self.find(v)
        if t1 != t2:
            for i in range(n):
                if self.parent[i] == t2:
                    self.parent[i] = t1
"""

if __name__ == "__main__":
    n = 10
    edges = [[1, 2], [3, 4], [5, 2], [4, 6], [2, 6], [8, 7], [9, 7], [1, 6], [2, 4]]
    s = Solution()
    print(s.countComponents(n, edges))