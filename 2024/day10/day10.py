import numpy as np
import heapq

def day10(filepath, part2=False):
    # return of the dirs
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def bfs(arr, root, part2=False):
        visited = set()
        q = []
        heapq.heappush(q, (0, root[0], root[1]))
        ans = 0
        
        while q:
            height, row, col = heapq.heappop(q)
            # print(visited)
            for d in dirs:
                new_row, new_col = row + d[0], col + d[1]
                if (new_row < 0 or new_row >= len(arr) or new_col < 0 or new_col >= len(arr)):
                    continue

                if arr[new_row][new_col] != height + 1:
                    continue
                if not part2 and (new_row, new_col) in visited:
                    continue
                
                if arr[new_row][new_col] == 9:
                    ans += 1
                heapq.heappush(q, (height+1, new_row, new_col))
                visited.add((new_row, new_col))
        return ans

    arr = []
    res = 0
    
    with open(filepath) as f:
        arr = np.array([list(int(x) for x in line.strip()) for line in f])

    roots = np.argwhere(arr == 0)
    for root in roots:
        if part2:
            res += bfs(arr, root, part2=True)
        else:
            res += bfs(arr, root)    
    return res

# assert day10('input_sample') == 36
# assert day10('input') == 538
print(day10('input', part2=True))
# time 0.230s