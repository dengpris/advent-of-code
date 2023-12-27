with open('input') as op:
    space = []
    rows_to_add = []
    cols_to_add = []
    galaxies = []

    for line in op:
        space.append(line.strip())
    
    for i, row in enumerate(space):
        if len(set(row)) == 1:
            rows_to_add.append(i)
            continue
        for j, c in enumerate(row):
            if c == '#':
                galaxies.append((i, j))
    
    transpose = [*zip(*space)]
    for j, col in enumerate(transpose):
        if len(set(col)) == 1:
            cols_to_add.append(j)
            continue

    distance = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            temp = 0
            temp += galaxies[j][0] - galaxies[i][0]
            temp += abs(galaxies[j][1] - galaxies[i][1])
            
            row_diff = list(range(galaxies[i][0], galaxies[j][0]))
            col_diff = list(range(min(galaxies[j][1], galaxies[i][1]), max(galaxies[j][1], galaxies[i][1])))
            
            for row in rows_to_add:
                if row in row_diff:
                    temp += 999999
                    
            for col in cols_to_add:
                if col in col_diff:
                    temp += 999999             
            distance += temp
    print(distance)