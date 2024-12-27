import numpy as np
import collections
import sys
from typing import List

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
def day20(filepath, cheats, part2=False) -> int:
    def is_valid(arr, row, col):
        if (row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0])):
            return False
        return True
    # For each reachable node in distance_from_start, travel manhattan distance of cheats (20)
    # If resulting node is reachable from finish, calculate new time
    def cheat(cheats: int, arr: List[str], distances_from_start: List[int], distances_from_finish: List[int]):
        def manhattan_dist(start, cheats, cheat_dict, arr) -> List[tuple]:
            dists = set()
            for drow in range(cheats+1):
                dcol = cheats - drow
                for dr in range(-1*drow, drow+1):
                    for dc in range(-1*dcol, dcol+1):
                        row, col = start[0] + dr, start[1] + dc
                        if not is_valid(arr, row, col):
                            continue
                        if (start, (row, col)) not in cheat_dict:
                            cheat_dict.add((start, (row, col)))
                            dists.add((abs(dr) + abs(dc), row, col))
            return dists
        
        diffs = collections.defaultdict(int)
        cheat_dict = set()
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if distances_from_start[row][col] == sys.maxsize:
                    continue
                # get manhattan distances
                dists = manhattan_dist((row, col), cheats, cheat_dict, arr)
                for time, r, c in dists:
                    if distances_from_finish[r][c] == sys.maxsize:
                        continue
                    new_score = distances_from_start[row][col] + time + distances_from_finish[r][c]
                    if new_score < score:
                        diffs[score - new_score] += 1
        return diffs

    def bfs(start: tuple[int, int], arr: List[str]) -> List[str]:   
        distances = [[sys.maxsize for _ in range(len(arr[0]))] for _ in range(len(arr))]
        distances[start[0]][start[1]] = 0
        q = collections.deque([start])
        while q:
            row, col = q.popleft()
            for d in dirs:
                new_row, new_col = row + d[0], col + d[1]
                if not is_valid(arr, new_row, new_col) or arr[new_row][new_col] == '#':
                    continue
                
                if distances[new_row][new_col] > distances[row][col] + 1:
                    q.append((new_row, new_col))
                    distances[new_row][new_col] = distances[row][col] + 1

        return distances
    
    with open(filepath) as f:
        arr = [list(line.strip()) for line in f.readlines()]
        arr = np.array(arr)

    start = tuple(np.argwhere(arr == 'S')[0])
    finish = tuple(np.argwhere(arr == 'E')[0])

    distances_from_start = bfs(start, arr)
    distances_from_finish = bfs(finish, arr)

    score = distances_from_start[finish[0]][finish[1]]
    diffs = cheat(cheats, arr, distances_from_start, distances_from_finish)

    out = 0
    for key, val in diffs.items():
        if key >= 100:
            # print(key, val)
            out += val
    return out
    
# assert day20('input', cheats=2) == 1521
print(day20('input', cheats=20))
# time: 1m15.353s
