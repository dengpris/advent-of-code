from collections import deque
import time

class Grid:
    def __init__(self):
        self.red_tiles = []
        self.areas = []
        self.compressed_tiles = []
        self.compressed_grid = []
        self.rows = []
        self.cols = []

    def add_red_tile(self, r, c):
        self.red_tiles.append((c, r))

    def get_all_areas(self):
        for i in range(len(self.red_tiles)):
            for j in range(i + 1, len(self.red_tiles)):
                p1 = self.red_tiles[i]
                p2 = self.red_tiles[j]
                area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
                self.areas.append((area, p1, p2))
        self.areas.sort(reverse=True)
        return self.areas

    def compress_tiles(self):
        self.rows = sorted(set([r for r, c in self.red_tiles]))
        self.cols = sorted(set([c for r, c in self.red_tiles]))
        row_map = {v: i for i, v in enumerate(self.rows)}
        col_map = {v: i for i, v in enumerate(self.cols)}
        for r, c in self.red_tiles:
            self.compressed_tiles.append((row_map[r], col_map[c]))


    def create_compressed_grid(self):
        max_r = max(r for r, c in self.compressed_tiles)
        max_c = max(c for r, c in self.compressed_tiles)
        self.compressed_grid = [['.' for _ in range(max_c + 1)] for _ in range(max_r + 1)]
        for r, c in self.compressed_tiles:
            self.compressed_grid[r][c] = '#'


    def fill_edges(self):
        for i in range(len(self.compressed_tiles)):
            if i == 0:
                r1, c1 = self.compressed_tiles[-1]
            else:
                r1, c1 = self.compressed_tiles[i-1]
            r2, c2 = self.compressed_tiles[i]
            
            if r1 == r2:
                for c in range(min(c1,c2), max(c1,c2)+1):
                    self.compressed_grid[r1][c] = '#'
            elif c1 == c2:
                for r in range(min(r1,r2), max(r1,r2)+1):
                    self.compressed_grid[r][c1] = '#'
        

    def get_first_inside_point(self):
        for y in range(len(self.compressed_grid)):
            prev_char = self.compressed_grid[y][0]
            boundary_crossings = 0

            for x in range(1, len(self.compressed_grid[0])):
                current_char = self.compressed_grid[y][x]
                if current_char != prev_char:
                    # '#' to '.' or '.' to '#'
                    boundary_crossings += 1

                prev_char = current_char
                if current_char == '.' and boundary_crossings % 2 == 1: 
                    return y, x  # Odd = inside
    
    def flood_fill(self):
        # bfsbfsbfs mwah mwah mwah
        r, c = self.get_first_inside_point()
        q = deque([(r, c)])
        self.compressed_grid[r][c] = '#'
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(self.compressed_grid) and 0 <= nc < len(self.compressed_grid[0]):
                    if self.compressed_grid[nr][nc] == '.':
                        self.compressed_grid[nr][nc] = '#'  # Mark as filled
                        q.append((nr, nc))


    def get_max_filled_rectangle(self):
        max_area = 0
        for i, vertex1 in enumerate(self.compressed_tiles):  # for each vertex self.compressed_tiles:
            for j, vertex2 in enumerate(self.compressed_tiles[i + 1:]):
                r1, c1 = vertex1
                r2, c2 = vertex2
                if r1 == r2 or c1 == c2:
                    continue
                r3, c3 = r2, c1
                r4, c4 = r1, c2
                # Check other two corners for quick reject
                if self.compressed_grid[r3][c3] != '#' or self.compressed_grid[r4][c4] != '#':
                    continue
                # Check inside (burte force)
                for r in range(min(r1, r2), max(r1, r2) + 1):
                    for c in range(min(c1, c2), max(c1, c2) + 1):
                        if self.compressed_grid[r][c] != '#':
                            break
                    else:
                        continue
                    break
                else:
                    r1, c1 = self.decompress_tile(r1, c1)
                    r2, c2 = self.decompress_tile(r2, c2)

                    max_area = max(max_area, (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1))
        
        return max_area
    
    def decompress_tile(self, r, c):
        return self.rows[r], self.cols[c]


def day9(filepath, part2=False):
    with open(filepath) as f:
        arr = [list(map(int, line.strip().split(','))) for line in f]
    
    g = Grid()
    for (r, c) in arr:
        g.add_red_tile(r, c)

    g.get_all_areas()

    if part2:
        max_area = 0
        g.compress_tiles()
        g.create_compressed_grid()
        g.fill_edges()
        g.flood_fill()
        max_area = g.get_max_filled_rectangle()
        return max_area

    return g.areas[0]

print(day9('input_sample', part2=False))
print(day9('input_sample', part2=True))

start = time.time()
print(day9('input', part2=True))
end = time.time()
print(end - start)