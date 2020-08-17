from collections import defaultdict
"""
students = 10
leads = 9
clues = [[1, 2], [3, 4], [5, 2], [4, 6], [2, 6], [8, 7], [9, 7], [1, 6], [2, 4]]
"""
class Unionfind():
    def __init__(self, students, leads, clues):
        self.students = students
        # Set up parent for each node.
        self.parent = {item:item for item in range(1, self.students + 1)}
        # Create a dictionary to store the group result.
        self.group = defaultdict(list)

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
            for i in range(1, self.students + 1):
                if self.parent[i] == t2:
                    self.parent[i] = t1
            #self.parent[t2] = t1

    def find_group(self, clues):
        for u, v in clues:
            self.union(u, v)

        for i in range(1, self.students + 1):
            self.group[self.parent[i]].append(i)
        
        return len(self.group)

def main():
    students = 10
    leads = 9
    clues = [[1, 2], [3, 4], [5, 2], [4, 6], [2, 6], [8, 7], [9, 7], [1, 6], [2, 4]]
    #clues = [[1, 2], [3, 4], [4, 5]]
    uf = Unionfind(students, leads, clues)
    print(uf.find_group(clues))

if __name__ == '__main__':
    main()