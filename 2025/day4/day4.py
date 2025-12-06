from collections import deque
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class Forklift:
    def __init__(self, grid):
        self.grid = grid
        self.r_len, self.c_len = len(grid), len(grid[0])
        self.reacheable = [[0 for x in range(self.c_len)] for y in range(self.r_len)] 
        

    def get_adjacent(self, r, c):
        adj = 0
        for d in dirs:
            new_r, new_c = r + d[0], c + d[1]
            if new_r < 0 or new_c < 0 or new_r >= self.r_len or new_c >= self.c_len:
                continue
            if self.grid[new_r][new_c] == '@':
                adj += 1
        self.reacheable[r][c] = adj
        return adj

    def populate_reachable(self):
        out = 0
        for x in range(self.r_len):
            for y in range(self.c_len):
                if self.grid[x][y] != '@':
                    continue
                if self.get_adjacent(x, y) < 4:
                    out += 1
        return out
    
    def remove_reachable(self):
        out = 0
        q = deque()
        for x in range(self.r_len):
            for y in range(self.c_len):
                if self.reacheable[x][y] < 4 and self.grid[x][y] == '@':
                    self.grid[x][y] = '.'
                    q.append((x,y)) 
        # BFS to update adjacent count            
        while len(q):
            x, y = q[0]
            q.popleft()
            if self.reacheable[x][y] < 4:
                out += 1
                self.update_adj(x, y, q)
        return out
    
    # Helper function for BFS
    def update_adj(self, r, c, q):
        for d in dirs:
            new_r, new_c = r + d[0], c + d[1]
            if new_r < 0 or new_c < 0 or new_r >= self.r_len or new_c >= self.c_len:
                continue    
            if self.grid[new_r][new_c] == '@':
                self.reacheable[new_r][new_c] -= 1
                if self.reacheable[new_r][new_c] < 4:
                    self.grid[new_r][new_c] = '.'
                    q.append((new_r, new_c))


def day4(filepath, part2=False):
    with open(filepath) as f:
        input_grid = [list(line.strip()) for line in f]
        forklift = Forklift(input_grid)
        out = forklift.populate_reachable()
        if part2:
            out = forklift.remove_reachable()
        return out

assert day4('input_sample', part2=False) == 13
assert day4('input_sample', part2=True) == 43
day4('input', part2=True)