from collections import deque

import functools

class Tachyon:
    def __init__(self, arr):
        self.grid = arr
        
    def get_start(self):
        for i, row in enumerate(self.grid):
            if 'S' in row:
                return (i, row.index('S'))

    @functools.cache            
    def recurse(self, r, c):
        if r >= len(self.grid):
            return 1
        if self.grid[r][c] == '^':
            return self.recurse(r+1, c+1) + self.recurse(r+1, c-1)
        return self.recurse(r+1,c)

    def traverse(self):
        q = {self.get_start()[1]}
        splits = 0
        curr_row = self.get_start()[0]
        while curr_row < len(self.grid):
            beams = set()
            for c in q:
                if c < len(self.grid[0]) and self.grid[curr_row][c] == '^':
                    splits += 1
                    if c - 1 not in beams:
                        beams.add(c - 1)
                    if c + 1 not in beams:
                        beams.add(c + 1)
                else:
                    if c not in beams:
                        beams.add(c)
            q = beams
            curr_row += 1
        return splits


def day7(filepath, part2=False):
    with open(filepath) as f:
        grid = [[c for c in line] for line in f.read().splitlines()]
    t = Tachyon(grid)
    if part2:
        return t.recurse(t.get_start()[0], t.get_start()[1])
    return t.traverse()


print(day7('input_sample'))
print(day7('input_sample', part2=True))
print(day7('input', part2=True))