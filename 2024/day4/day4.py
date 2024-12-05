import numpy as np
import re

def day4(filepath, part2=False):
    data = np.genfromtxt(filepath, dtype=str)
    arr = np.array([list(line) for line in data])
    rows = [''.join(arr[i, :]) for i in range(arr.shape[0])]
    cols = [''.join(arr[:, i]) for i in range(arr.shape[1])]
    diag_right = [''.join(np.diagonal(arr, offset=i)) for i in range(-1 * arr.shape[0]+1, arr.shape[0])]
    diag_left = [''.join(np.diagonal(arr[:,::-1], offset=i)) for i in range(-1 * arr.shape[0]+1, arr.shape[0])]

    res: int = 0
    if part2:
        # we will keep track of the position of 'a' (the intersection of x-mas)
        pos = []
        for i, line in enumerate(diag_right):
            found = re.finditer('(?=(MAS|SAM))', line)
            for it in found:
                j = it.span()[0]
                if i < len(arr): # bottom half
                   pos.append((i-j-1, j+1))
                else: # top half
                   pos.append((len(arr)-j-2, i-len(arr)+j+2))
        # for each coords in found, check +1, +1 and -1, -1
        # reverse the array bc im silly
        arr = arr[::-1]
        for p in pos:
            i, j = p
            if i > 0 and j > 0 and i < len(arr)-1 and j < len(arr[0])-1:
                if arr[i+1][j+1] == 'M' and arr[i-1][j-1] == 'S':
                    res += 1
                elif arr[i+1][j+1] == 'S' and arr[i-1][j-1] == 'M':
                    res += 1
    else:
        # check rows
        for line in rows:
            res += len(re.findall('(?=(XMAS|SAMX))', line))
        # check cols
        for line in cols:
            res += len(re.findall('(?=(XMAS|SAMX))', line))
        # check diagonals
        for line in diag_right:
            res += len(re.findall('(?=(XMAS|SAMX))', line))
        for line in diag_left:
            res += len(re.findall('(?=(XMAS|SAMX))', line))

    return res

print(day4('input', part2=True))