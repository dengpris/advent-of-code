import numpy as np
import heapq
import sys
import collections

dirs = {
    '^': np.array([-1,0]),
    'v': np.array([1,0]),
    '<': np.array([0,-1]),
    '>': np.array([0,1])
}

def day16(filepath, part2=False):    
    def get_path(arr, parents, start, finish):
        path = []
        q = [finish]
        while q:
            y, x, d = q.pop()
            path.append((y, x, d))
            q.extend(parents[(y, x, d)])
        path.append((start[0], start[1], '^'))
        return path

    def dijkstras(arr, start, finish, benches=None, score=None):
        parents = collections.defaultdict(list)
        visited = [[{ '^': sys.maxsize, 'v': sys.maxsize, '<': sys.maxsize, '>': sys.maxsize } for _ in range(len(arr[0]))] for _ in range(len(arr))]
        y, x = start
        visited[y][x]['>'] = 0
        q = [(y, x, '>')]
        heapq.heapify(q)
        while len(q):
            y, x, d = heapq.heappop(q)
            if score and visited[y][x][d] > score:
                continue
            # option 1: keep going in direction
            new_y, new_x = (y, x) + dirs[d]
            if arr[new_y][new_x] != '#' and visited[new_y][new_x][d] >= visited[y][x][d] + 1:
                if visited[new_y][new_x][d] > visited[y][x][d] + 1:
                    visited[new_y][new_x][d] = visited[y][x][d] + 1
                    heapq.heappush(q, (new_y, new_x, d))
                    parents[(new_y, new_x, d)] = []
                parents[(new_y, new_x, d)].append((y,x,d))
            # option 2: change directions
            for new_d in dirs:
                if new_d == d:
                    continue
                if visited[y][x][new_d] >= visited[y][x][d] + 1000:
                    if visited[y][x][new_d] > visited[y][x][d] + 1000:
                        visited[y][x][new_d] = visited[y][x][d] + 1000
                        heapq.heappush(q, (y, x, new_d))
                        parents[(y, x, new_d)] = []
                    parents[(y, x, new_d)].append((y,x,d))
        # check: what is the smallest number at finish?
        y, x = finish
        res = sys.maxsize
        for d, total in visited[y][x].items():
            res = min(res, total)
            if score:
                finish = (finish[0], finish[1], d)
                path = get_path(arr, parents, start, finish)
                for y, x, d in path:
                    benches[y][x] = 1
                print(benches)
        return res
        

    arr = []
    with open(filepath) as f:
        lines = [list(line.strip()) for line in f]
        arr = np.array(lines)
    
    start = np.argwhere(arr == 'S')[0]
    finish = np.argwhere(arr == 'E')[0]
    score = dijkstras(arr, start, finish)
    
    if part2:
        benches = np.zeros(arr.shape, dtype=int)
        dijkstras(arr, start, finish, benches, score)

        return np.count_nonzero(benches)

    return score

# assert day16('input_sample') == 7036
# assert day16('input_sample_2') == 11048
# assert day16('input') == 95476
# print(day16('input_sample', part2=True))
# print(day16('input_sample_2', part2=True))
print(day16('input', part2=True))
# time: 4.002s