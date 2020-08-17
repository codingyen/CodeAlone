from collections import defaultdict

class UnionFind():
    def __init__(self, pairs):
        self.items = set()
        for a, b in pairs:
            self.items.add(a)
            self.items.add(b)
        self.parent = {item:item for item in self.items}
        self.group = defaultdict(list)

    def find(self, v):
        if self.parent[v] == v:
            return v
        else:
            self.parent[v] = self.find(self.parent[v])
            return self.parent[v]


    def union(self, u, v):
        t1 = self.find(u)
        t2 = self.find(v)
        if t1 != t2:
            for i in self.items:
                if self.parent[i] == t2:
                    self.parent[i] = t1
            #self.parent[t2] = t1

    def find_largest_group(self, pairs):
        for u, v in pairs:
            self.union(u, v)
        
        for item in self.items:
            self.group[self.parent[item]].append(item)
        
        maxGroup = []

        for group in self.group.values():
            if len(maxGroup) < len(group):
                maxGroup = group
        return maxGroup


def main():
    pairs = [["Item1", "Item2"], ["Item3", "Item4"], ["Item4", "Item5"]]
    uf = UnionFind(pairs)
    print(uf.find_largest_group(pairs))

if __name__ == "__main__":
    main()