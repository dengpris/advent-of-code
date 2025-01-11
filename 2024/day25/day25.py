import numpy as np

def day25(filepath, part2=False):
    locks = []
    keys = []
    with open(filepath) as f:
        schematics = f.read().split('\n\n')
        for schematic in schematics:
            arr = np.array([list(x) for x in schematic.split('\n')])
            cols = [''.join(arr[:, i]) for i in range(arr.shape[1])]
            height = [col.count('#')-1 for col in cols]
            # Locks start with #####
            locks.append(height) if arr[0][0] == '#' else keys.append(height)

    out = 0
    # Simple loop over each lock and key
    for lock in locks:
        for key in keys:
            for l, k in zip(lock, key):
                if l+k > 5: break
            else: out += 1

    return out

assert day25('input_sample') == 3
print(day25('input'))