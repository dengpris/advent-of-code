import numpy as np
import collections
import sys

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

def day18(filepath, bytes, part2=False):
    def dijkstras(arr, start, finish):
        visited = [[sys.maxsize for _ in range(len(arr[0]))] for _ in range(len(arr))]
        visited[start[0]][start[1]] = 0
        q = collections.deque([start])
        
        while q:
            row, col = q.popleft()
            for d in dirs:
                new_row, new_col = row + d[0], col + d[1]
                if (new_row < 0 or new_row >= len(arr) or new_col < 0 or new_col >= len(arr)):
                    continue

                if arr[new_row][new_col] == -1:
                    continue
                
                if visited[new_row][new_col] > visited[row][col] + 1:
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = visited[row][col] + 1
        
        return visited[finish[0]][finish[1]]
    
    n = 71
    if 'sample' in filepath:
        n = 7
    arr = np.zeros((n, n), dtype=int)
    lines = []
    
    with open(filepath) as f:
        lines = f.readlines()
        i = 0
        while i < bytes:
            line = lines[i]
            y, x = map(int, line.split(','))
            arr[y][x] = -1
            i += 1

    start = (0,0)
    finish = (n-1, n-1)

    if not part2:
        return dijkstras(arr, start, finish)
    
    while dijkstras(arr, start, finish) != sys.maxsize:
        line = lines[i]
        y, x = map(int, line.split(','))
        arr[y][x] = -1
        i += 1
    
    return lines[i-1]

# assert day18('input_sample', 12) == 22
# assert day18('input', 1024) == 226
print(day18('input', 1024, part2=True))
# time: 7.310s