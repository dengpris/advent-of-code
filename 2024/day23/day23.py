import collections
import math
import itertools

def day23(filepath, part2=False):
    def is_clique(arr, conn):
        for item in arr:
            if set(arr).issubset(([item] + conn[item])):
                continue
            return False
        return True
    
    conn = collections.defaultdict(list)
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            u, v = line.split('-')
            conn[u].append(v)
            conn[v].append(u)
    
    combinations = set()
    max_size = 0
    out = 0

    for key, val in conn.items():
        if not part2:
            for comb in itertools.combinations(val, 2):
                comb += (key,)
                comb = tuple(sorted(comb))
                if comb not in combinations and is_clique(comb, conn):
                    combinations.add(comb)
                    for c in comb:
                        if c[0] == 't':
                            out += 1
                            break
        else:
            for size in range(len(val), max_size-1, -1):
                for comb in itertools.combinations(val, size):
                    comb += (key,)
                    if is_clique(comb, conn) and max_size < len(comb):
                        max_size = len(comb)
                        combinations = comb
    if part2:
        return sorted(combinations)
    
    return out


assert day23('input_sample') == 7
assert day23('input') == 1108
# print(day23('input_sample', part2=True))
print(day23('input', part2=True))
# time: 0.338s