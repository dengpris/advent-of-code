import collections
from functools import cache
import sys

# wow so hard >_<
def day21(filepath, part2=False):
    def create_moves(arr):
        # get positions of all buttons
        pos = collections.defaultdict(tuple)
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                key = arr[row][col]
                pos[key] = (row, col)
            
        # get moves for each combination: e.g. ('^', '>), (9, 7)
        moves = collections.defaultdict(list)
        for key1 in pos:
            for key2 in pos:
                if key1 is None or key2 is None:
                    continue
                k1_row, k1_col = pos[key1]
                k2_row, k2_col = pos[key2]
                
                if k1_row == k2_row:
                    d = '>' if k2_col > k1_col else '<'
                    moves[(key1, key2)] = [abs(k2_col-k1_col) * d + 'A']
                elif k1_col == k2_col:
                    d = 'v' if k2_row > k1_row else '^'
                    moves[(key1, key2)] = [abs(k2_row-k1_row) * d + 'A']
                else:
                    if k1_col != pos[None][1] or k2_row != pos[None][0]: # go vertical first
                        d1 = 'v' if k2_row > k1_row else '^'
                        d2 = '>' if k2_col > k1_col else '<'
                        moves[(key1, key2)].append(abs(k2_row-k1_row) * d1 + abs(k2_col-k1_col) * d2 + 'A')
                    if k1_row != pos[None][0] or k2_col != pos[None][1]:
                        d1 = '>' if k2_col > k1_col else '<'
                        d2 = 'v' if k2_row > k1_row else '^'
                        moves[(key1, key2)].append(abs(k2_col-k1_col) * d1 + abs(k2_row-k1_row) * d2 + 'A')
        return moves
    
    moves = [] # initialize our variable for mapping moves

    def build_move(move_string, idx, curr_path):
        res = []
        if idx == len(move_string):
            return [curr_path]
        currKey = move_string[idx]
        prevKey = 'A' if idx == 0 else move_string[idx-1]
        for move in moves[(prevKey, currKey)]:
            steps = (build_move(move_string, idx+1, curr_path + move))
            res.extend(steps)
        return res

    @cache
    def find_shortest(move_string, depth):
        if depth == 0:
            return len(move_string)
        
        submoves = move_string.split('A')
        res = 0
        for i, submove in enumerate(submoves):
            if i != len(submoves)-1:
                submove += 'A'
            builds = build_move(submove, idx=0, curr_path='')
            minimum = sys.maxsize
            for build in builds:
                minimum = min(minimum, find_shortest(build, depth-1))
            res += minimum
        return res

            
    # Day21 solution
    with open(filepath) as f:
        arr = [line.strip() for line in f]
    
    keypad = [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
        [None, '0', 'A']
    ]
    dirpad = [
        [None, '^', 'A'],
        ['<', 'v', '>']
    ]
    key_moves = create_moves(keypad)
    dir_moves = create_moves(dirpad)
    moves = { **key_moves, ** dir_moves} # combine keypad and directional pads
    max_depth = 25 if part2 else 2

    out = 0
    for code in arr:
        num = int(code[:3])
        builds = build_move(code, idx=0, curr_path='')
        minimum = sys.maxsize
        for build in builds:
            minimum = min(minimum, find_shortest(build, max_depth))
        out += (minimum) * num
    return out

print(day21('input_sample'))
print(day21('input', part2=True))
# time: 0.328s