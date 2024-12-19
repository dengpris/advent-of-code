import numpy as np
import collections

dirs = {
    '^': np.array([-1,0]),
    'v': np.array([1,0]),
    '<': np.array([0,-1]),
    '>': np.array([0,1])
}
# day 15 is making me so sad :(((((wow my sad face turned into brackets)))))
# first pretty hard day imo
def day15(filepath, part2=False):
    # check if push is valid
    def push(arr, d, loc):
        y, x = loc
        arr[y][x] = '.'
        while True:
            y, x = [y, x] + dirs[d]
            # if push not valid, we stay in same place
            if arr[y][x] == '#':
                return loc
            # update the final box loc and also the start
            if arr[y][x] == '.':
                arr[y][x] = 'O'
                pos_y, pos_x = loc + dirs[d]
                arr[pos_y][pos_x] = '@'
                return (pos_y, pos_x)


    # dfs (normally i am bfs-head but today we dfs)
    def dfs(arr, visited, d, loc):
        y, x = loc
        if arr[y][x] == '#':
            visited[y][x] = 0 # false
        if arr[y][x] == '.':
            visited[y][x] = 1
        if visited[y][x] != -1:
            return visited[y][x]
        
        y, x = [y, x] + dirs[d]
        is_valid = dfs(arr, visited, d, [y,x])
        if d == 'v' or d == '^':
            if arr[y][x] == '[':
                is_valid = is_valid and dfs(arr, visited, d, [y, x+1])
            elif arr[y][x] == ']':
                is_valid = is_valid and dfs(arr, visited, d, [y, x-1])
        return is_valid

    def update_lr(arr, d, loc):
        y, x = loc
        arr[y][x] = '.'
        y, x = loc + dirs[d]
        tmp = arr[y][x]
        arr[y][x] = '@'
        if tmp == '.':
            return
        
        while True:
            y, x = [y, x] + dirs[d]
            # update the final box loc and also the start
            if arr[y][x] == ']':
                arr[y][x] = '['
            elif arr[y][x] == '[':
                arr[y][x] = ']'
            else:
                if d == '>':
                    arr[y][x] = ']'
                else:
                    arr[y][x] = '['
                break

    def update_ud(arr, d, loc):
        to_update = set()
        q = collections.deque()
        y, x = loc
        q.append((y, x, '@'))
        arr[y][x] = '.'
        # traverse through values to update
        while len(q):
            y, x, val = q.popleft()
            arr[y][x] = '.' # reset value
            y, x = (y, x) + dirs[d]
            # we need to account for the '.' since @ will only push one side
            if val == '@':
                if arr[y][x] == '[':
                    to_update.add((y,x+1,'.'))
                elif arr[y][x] == ']':
                    to_update.add((y,x-1,'.'))
            if arr[y][x] != '.':
                if arr[y][x] == '[':
                    q.append((y, x+1, ']'))
                elif arr[y][x] == ']':
                    q.append((y, x-1, '['))     
                q.append((y,x, arr[y][x]))
            to_update.add((y, x, val))
        # update graph with new vals
        for y, x, val in to_update:
            arr[y][x] = val
            
    is_dir = False
    path = ''
    arr = []
    with open(filepath) as f:
        for line in f:
            if not len(line.strip()):
                is_dir = True
                continue
            if is_dir:
                path += line.strip()
            else:
                if part2:
                    tmp = []
                    for i in list(line.strip()):
                        if i == '@':
                            tmp.extend('@.')
                        elif i == 'O':
                            tmp.extend('[]')
                        elif i == '#':
                            tmp.extend('##')
                        else:
                            tmp.extend('..')
                    arr.append(tmp)
                else:
                    arr.append(list(line.strip()))
            
    path = np.array(list(path))
    arr = np.array(arr)
    # print(path)
    # print(arr)
    loc = np.argwhere(arr == '@')[0]
        
    with open('out.txt', 'w') as f:
        for d in path:
            if part2:
                visited = [[-1 for _ in range(len(arr[0]))] for _ in range(len(arr))]
                is_valid = dfs(arr, visited, d, loc)
                if is_valid:
                    if d == '<' or d == '>':
                        update_lr(arr, d, loc)
                    else:
                        update_ud(arr, d, loc)
                    loc = loc + dirs[d]
            else:
                loc = push(arr, d, loc)
            # for a in arr:
                # print(''.join(a), file=f)
            # print(d, file=f)
            # print(loc, file=f)
            # print('', file=f)
    
    res = 0
    boxes = np.argwhere(arr == 'O')

    if part2:
        boxes = np.argwhere(arr == '[')
    
    for y, x in boxes:
        res += 100 * y + x
    
    return res

# assert day15('input_sample', part2=True) == 2028
assert day15('input_sample_2', part2=True) == 9021
# print(day15('test', part2=True))
print(day15('input', part2=True))
# time 1.316s