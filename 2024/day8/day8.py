import numpy as np
import collections

def day8(filepath, part2=False):
    with open(filepath) as f:
        antennas = collections.defaultdict(list)
        lines = [list(line.strip()) for line in f]
        arr = np.array(lines)
        res = 0

        # find all antennas
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if arr[i][j] != '.':
                    antennas[arr[i][j]].append((i, j))

        # find antinodes of each tower frequency
        for val in antennas.values():
            if part2 and len(val) > 1:
                res += len(val)
            for i in range(len(val)-1):
                for j in range(i+1, len(val)):
                    ant1, ant2 = val[i], val[j]
                    diff = tuple(a - b for a, b in zip(ant1, ant2))
                    
                    node1 = tuple(map(sum, zip(ant1, diff)))
                    node2 = tuple(a - b for a, b in zip(ant2, diff))

                    if not part2:
                        if node1[0] >= 0 and node1[0] < len(arr) and node1[1] >= 0 and node1[1] < len(arr[0]):
                            row, col = node1
                            if arr[row][col] != '#':
                                arr[row][col] = '#'
                                res += 1
                        if node2[0] >= 0 and node2[0] < len(arr) and node2[1] >= 0 and node2[1] < len(arr[0]):
                            row, col = node2
                            if arr[row][col] != '#':
                                arr[row][col] = '#'
                                res += 1
                        continue
                        
                    while node1[0] >= 0 and node1[0] < len(arr) and node1[1] >= 0 and node1[1] < len(arr[0]):
                        row, col = node1
                        if arr[row][col] == '.':
                            arr[row][col] = '#'
                            res += 1
                        node1 = tuple(map(sum, zip(node1, diff)))

                    while node2[0] >= 0 and node2[0] < len(arr) and node2[1] >= 0 and node2[1] < len(arr[0]):
                        row, col = node2
                        if arr[row][col] == '.':
                            arr[row][col] = '#'
                            res += 1
                        node2 = tuple(a - b for a, b in zip(node2, diff))

        return res

print(day8('input', part2=False))
# time: 0.213s