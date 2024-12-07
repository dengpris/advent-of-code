import numpy as np

dirs = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

turn_right = {
    'up': 'right',
    'down': 'left',
    'left': 'up',
    'right': 'down'
}

def day6(filepath, part2=False):
    def traverse(arr, pos):
        (row, col), d = pos
        # initial action: continue in same direction
        new_row, new_col = tuple(map(sum, zip((row, col), dirs[d])))
        # out of bounds
        if new_row >= len(arr) or new_row < 0 or new_col >= len(arr[0]) or new_col < 0:
            return ((-1, -1), d)
        # found obstacle, recalculating position
        if arr[new_row][new_col] == '#':
            d = turn_right[d]
            # new_row, new_col = tuple(map(sum, zip((row, col), dirs[d])))
            return ((row, col), d)
        return ((new_row, new_col), d)
    
    def is_loop(arr, pos):
        # 1952 too high
        visited = set(pos)
        while True:
            (row, col), d = traverse(arr, pos)
            if ((row, col), d) in visited:
                return 1
            if (row, col) == (-1, -1):
                return 0
            visited.add(((row, col), d))
            pos = ((row, col), d)

    with open(filepath) as f:
        lines = [list(line.strip()) for line in f]
        arr = np.array(lines)
        
        # Find starting pos
        start = tuple(np.argwhere(arr=='^')[0])
        pos = (start, 'up')
        res = 1
        
        # Simulate path
        visited = set() # part 2, track pos of all nodes visited
        while True:
            (row, col), d = traverse(arr, pos)
            if (row, col) == (-1, -1):
                break
            if (row, col) not in visited:
                visited.add((row, col))
                res += 1
            pos = ((row, col), d)

        if part2:
            res = 0
            # let us put an obstacle in every node of the path
            for obs_row, obs_col in visited:
                arr[obs_row][obs_col] = '#'
                res += is_loop(arr, (start, 'up'))
                arr[obs_row][obs_col] = '.'

        return res
    
print(day6('input', part2=True))
# time: 1m0.416s