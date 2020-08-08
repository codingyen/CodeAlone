class Solution:
    def criticalConnections(self, n, connections):
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        lookup = [-1] * n 

        def dfs(par, curr, lvl, lookup, g, res):
            lookup[curr] = lvl + 1
            for child in g[curr]:
                if child == par:
                    continue
                elif lookup[child] == -1:
                    lookup[curr] = min(lookup[curr], dfs(curr, child, lvl + 1, lookup, g, res))
                else:
                    lookup[curr] = min(lookup[curr], lookup[child])

            if lookup[curr] == lvl + 1 and curr != 0:
                res.append([par, curr])
            return lookup[curr]

        res = []
        dfs(-1, 0, 0, lookup, g, res)
        return res

if __name__ == '__main__':
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    s = Solution()
    print(s.criticalConnections(n, connections))