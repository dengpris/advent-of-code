import math

# Disjoint set
class JunctionBox:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False
        
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i

        self.size[root_i] += self.size[root_j]
        self.parent[root_j] = root_i
        return True 
    
    def get_sets(self):
        sets = {}
        for i in range(len(self.size)):
            parent = self.find(i)
            sets.setdefault(parent, []).append(i)
        return sorted([len(sets[key]) for key in sets.keys()])

class Grid:
    def __init__(self):
        self.points = {}
        self.distances = []

    def add_point(self, point_id, x, y, z):
        self.points[point_id] = (x, y, z)

    def get_point_coordinates(self, point_id):
        if point_id in self.points:
            return self.points[point_id]
        else:
            raise ValueError(f"Point ID {point_id} not found in the grid.")

    def get_all_distances(self):
        for i in range(len(self.points)):
            for j in range(i, len(self.points)):
                if i == j:
                    continue
                p1 = self.get_point_coordinates(i)
                p2 = self.get_point_coordinates(j)
                distance = math.dist(p1, p2)
                self.distances.append((distance, i, j))


def day8(filepath, part2=False):
    with open(filepath) as f:
        arr = [list(map(int, line.strip().split(','))) for line in f]
    
    g = Grid()
    for i, (x, y, z) in enumerate(arr):
        print(i,x,y,z)
        g.add_point(i, x, y, z)
    
    g.get_all_distances()
    g.distances.sort()
    
    u = JunctionBox(len(arr))

    if part2:
        for i in range(len(g.distances)):
            d, p1, p2 = g.distances[i]
            if u.union(p1, p2):
                res = g.points[p1][0] * g.points[p2][0]
        
        return res
    
    else:
        for i in range(1000):
            d, p1, p2 = g.distances[i]
            u.union(p1, p2)
            sets = u.get_sets()
        
    return sets[-1] * sets[-2] * sets[-3]

print(day8('input', part2=True))