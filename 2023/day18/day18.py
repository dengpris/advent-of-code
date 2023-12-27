import numpy as np
def direction(n):
    if n == 0:
        return 'R'
    elif n == 1:
        return 'D'
    elif n == 2:
        return 'L'
    else:
        return 'U'

def day18(filepath, part2=False):
    # total_row, total_col = 1, 1
    (row, col) = (0, 0)
    lagoon = np.array([['#']])
    start = [0, 0]
    instructions = []
    with open(filepath) as f:
        # build lagoon
        for line in f:
            d, s, colour = line.strip().split() # direction, steps, colour
            s = int(s)
            if part2:
                colour = colour[2:-1]
                s = int(colour[:-1], 16)
                d = direction(int(colour[-1]))
            instructions.append((d, s))
            if d == 'R':
                # total_col += s
                if not part2:
                    if len(lagoon[0]) - 1 < col + s:
                        for _ in range(col + s + 1 - len(lagoon[0])):
                            lagoon = np.c_[lagoon, np.full(len(lagoon), '.')]
                    for c in range(col, col + s + 1):
                        lagoon[row][c] = '#'
                col += s
            elif d == 'L':
                # total_col -= s
                if col - s < 0:
                    start[1] += s - col
                    if not part2:
                        for _ in range(col - s, 0):
                            lagoon = np.c_[np.full(len(lagoon), '.'), lagoon]
                        for c in range(0, s + 1):
                            lagoon[row][c] = '#'
                    col = 0
                    continue
                if not part2:
                    for c in range(col, col - s - 1, -1):
                        lagoon[row][c] = '#'
                col -= s
            elif d == 'D':
                if not part2:
                    if len(lagoon) - 1 < row + s:
                        for _ in range(row + s + 1 - len(lagoon)):
                            lagoon = np.r_[lagoon, [np.full(len(lagoon[0]), '.')]]
                    for r in range(row, row + s + 1):
                        lagoon[r][col] = '#'
                row += s
            else:
                if row - s < 0:
                    start[0] += s - row
                    if not part2:
                        for _ in range(row - s, 0):
                            lagoon = np.r_[[np.full(len(lagoon[0]), '.')], lagoon]
                        for r in range(0, s + 1):
                            lagoon[r][col] = '#'
                    row = 0
                    continue
                if not part2:
                    for r in range(row, row - s - 1, -1):
                        lagoon[r][col] = '#'
                row -= s

    # for _ in lagoon:
    #     print(_)
    
    vertices = []
    curr = [start[0], start[1]]
    b = 0
    print(instructions)
    for i in instructions:
        d = i[0]
        s = i[1]
        b += s
        if d == 'U':
            curr[0] -= s
        elif d == 'D':
            curr[0] += s
        elif d == 'L':
            curr[1] -= s
        else:
            curr[1] += s
        vertices.append(curr.copy())
        
    total = 0
    #combine shoelace with pick's theorem
    # A = i + b/2 - 1 -> A + b/2 + 1 = i + b
    vertices.reverse()
    for i in range(len(vertices)):
        if i == len(vertices) - 1:
            total += (vertices[i][0] * vertices[0][1] - vertices[i][1] * vertices[0][0])
            continue
        total += (vertices[i][0] * vertices[i+1][1] - vertices[i][1] * vertices[i+1][0])

    return (total + b) // 2 + 1

print(day18('input', part2=True))