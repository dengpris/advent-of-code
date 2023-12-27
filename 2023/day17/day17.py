with open('input') as f:
    # initalize map
    Grid = [];
    for line in f:
        temp = []
        for c in line.strip():
            temp.append(int(c))
        Grid.append(temp)
    m = len(Grid) - 1
    n = len(Grid[0]) - 1

    def get_neighbours(node: tuple) -> list:
        # our nodes are (x, y, d, s) -> (row, col, direction, # of straight travelled)
        neighbours = []
        row, col, d, s = node
        arr = []
        if (d == 'N'):
            if s < 10:
                arr.append((row-1, col, 'N', s+1))
            if s >= 4:
                arr.extend([(row, col-1, 'W', 1), (row, col+1, 'E', 1)])
        elif (d == 'S'):
            if s < 10:
                arr.append((row+1, col, 'S', s+1))
            if s >= 4:
                arr.extend([(row, col-1, 'W', 1), (row, col+1, 'E', 1)])
        elif (d == 'W'):
            if s < 10:
                arr.append((row, col-1, 'W', s+1))
            if s >= 4:
                arr.extend([(row-1, col, 'N', 1), (row+1, col, 'S', 1)])
        elif (d == 'E'):
            if s < 10:
                arr.append((row, col+1, 'E', s+1))
            if s >= 4:
                arr.extend([(row-1, col, 'N', 1), (row+1, col, 'S', 1)])
        else:
            raise(RuntimeError)
        
        for v in arr:
            if v[0] >= 0 and v[0] <= m and v[1] >=0 and v[1] <= n:
                    neighbours.append(v)
        return neighbours
    
    def heuristic(node) -> float:
        return abs(node[0] - m) + abs(node[1] - n)
    
    # A* algorithm: f(n) = g(n) + h(n)
    # let h = |x_start - x_end| + |y_start - y_end|
    def AStarSearch(start: tuple, end: tuple) -> list:
        openSet = set()
        openSet.add((0, 0, 'E', 0))
        closedSet = set()
        g = {} # cost from start
        parents = {}

        g[(0, 0, 'E', 0)] = 0
        parents[(0, 0, 'E', 0)] = (0, 0, 'E', 0)
        while len(openSet) > 0:
            curr = None
            # print(openSet)
            for v in openSet:
                if curr == None or g[v] + heuristic(v) < g[curr] + heuristic(curr):
                    curr = v
            if (curr[0], curr[1]) == end or Grid[curr[0]][curr[1]] == None:
                pass
            else:
                for node in get_neighbours(curr):
                    # (row, col, d, s)
                    weight = Grid[node[0]][node[1]]
                    if node not in openSet and node not in closedSet:
                        openSet.add(node)
                        parents[node] = curr
                        g[node] = g[curr] + weight
                    else:
                        if g[node] > g[curr] + weight:
                            #update g(node)
                            g[node] = g[curr] + weight
                            #change parent of node to n
                            parents[node] = curr
                             
                            #if node in closed set, remove and add to open
                            if node in closedSet:
                                closedSet.remove(node)
                                openSet.add(node)
            
            if (curr[0], curr[1]) == end and curr[3] >= 4:
                print(g[curr])
                path = []
                while parents[curr] != curr:
                    # print(g[curr])
                    path.append(curr)
                    curr = parents[curr]
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
            
            openSet.remove(curr)
            closedSet.add(curr)
    AStarSearch((0, 0), (m, n))