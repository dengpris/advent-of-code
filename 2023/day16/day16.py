grid = []
with open('input') as f:
    def go_straight(row, col, d):
        if d == 'N':
            row -= 1
        elif d == 'S':
            row += 1
        elif d == 'W':
            col -= 1
        elif d == 'E':
            col += 1
        return (row, col, d)
    
    def turn_left(row, col, d):
        if d == 'N':
            d = 'W'
            col -= 1
        elif d == 'S':
            d = 'E'
            col += 1
        elif d == 'W':
            d = 'S'
            row += 1
        elif d == 'E':
            d = 'N'
            row -= 1
        return (row, col, d)

    def turn_right(row, col, d):
        if d == 'N':
            d = 'E'
            col += 1
        elif d == 'S':
            d = 'W'
            col -= 1
        elif d == 'W':
            d = 'N'
            row -= 1
        elif d == 'E':
            d = 'S'
            row += 1
        return (row, col, d)
    
    def check_bounds(x, y):
        if x < 0 or x == len(grid):
            return False
        if y < 0 or y == len(grid[0]):
            return False
        return True
    
    for line in f:
        row = []
        for c in line.strip():
            row.append(c)
        grid.append(row)
    
    start = []
    out = 0
    for i in range(len(grid[0])):
        start.append((0, i, 'S'))
        start.append((len(grid) - 1, i, 'N'))
    for i in range(1, len(grid) - 1):
        start.append((i, 0, 'E'))
        start.append((i, len(grid[0]) - 1, 'W'))
    for s in start:
        visited = set()
        prev = [s] # (pos_x, pos_y, dir)
        while (prev):
            curr = []
            for i in prev:
                row = i[0]
                col = i[1]
                d = i[2]
                
                if not check_bounds(row, col):
                    continue
                
                if (row, col, d) in visited:
                    continue
                # print(i)
                visited.add((row, col, d))
                if (grid[row][col] == '.'):
                    curr.append(go_straight(row, col, d))
                elif (grid[row][col] == '\\'):
                    if d == 'N' or d == 'S':
                        curr.append(turn_left(row, col, d))
                    else:
                        curr.append(turn_right(row, col, d))
                elif (grid[row][col] == '/'):
                    if d == 'N' or d == 'S':
                        curr.append(turn_right(row, col, d))
                    else:
                        curr.append(turn_left(row, col, d))
                elif (grid[row][col] == '|'):
                    if d == 'N' or d == 'S':
                        curr.append(go_straight(row, col, d))
                    else:
                        curr.append(turn_left(row, col, d))
                        curr.append(turn_right(row, col, d))
                elif (grid[row][col] == '-'):
                    if d == 'W' or d == 'E':
                        curr.append(go_straight(row, col, d))
                    else:
                        curr.append(turn_left(row, col, d))
                        curr.append(turn_right(row, col, d))
            prev = curr.copy()

        output = set()
        for i in visited:
            output.add((i[0], i[1]))
        out = max(out, len(output))
    print(out)
 