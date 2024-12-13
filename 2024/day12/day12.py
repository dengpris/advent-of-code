import numpy as np
import heapq
import collections

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
def day12(filepath, part2=False):
    def bfs(arr, visited, letter, start) -> set:
        out = [start]
        q = [start]
        heapq.heapify(q)
        while q:
            row, col = heapq.heappop(q)
            for d in dirs:
                new_row, new_col = row + d[0], col + d[1]
                if (new_row < 0 or new_row >= len(arr) or new_col < 0 or new_col >= len(arr)):
                    continue
                if visited[new_row][new_col] or arr[new_row][new_col] != letter:
                    continue
                
                heapq.heappush(q, (new_row, new_col))
                visited[new_row][new_col] = 1
                out.append((new_row, new_col))
        
        return out
    
    def get_perimeter(arr, letter, sub_region):
        perimeter = 0
        sub_region.sort()
        # add 4 for each garden plot, subtract sides as needed
        for row, col in sub_region:
            perimeter += 4
            # since we are going left->right and up->down, let's check previous neighbours (left, up) to see if they share a wall
            if (row-1 >= 0 and arr[row-1][col] == letter):
                perimeter -= 2
            if (col-1 >= 0 and arr[row][col-1] == letter):
                perimeter -= 2
        
        return perimeter
    
    def get_sides(arr, letter, sub_region):
        corners = 0
        sub_region.sort()
        if len(sub_region) == 1:
            return 4
        for row, col in sub_region:
            right, left, up, down = 0,0,0,0
            if row + 1 < len(arr) and arr[row + 1][col] == letter:
                down = 1
            if row - 1 >= 0 and arr[row - 1][col] == letter:
                up = 1
            if col + 1 < len(arr[0]) and arr[row][col + 1] == letter:
                right = 1
            if col - 1 >= 0 and arr[row][col - 1] == letter:
                left = 1
            # four connected sides is four inverted corners
            # need to verify based on diagonals
            connected = sum((left, right, up, down))
            if connected == 4:
                corners += 4
                if arr[row-1][col-1] == letter:
                    corners -= 1
                if arr[row+1][col+1] == letter:
                    corners -= 1
                if arr[row+1][col-1] == letter:
                    corners -= 1
                if arr[row-1][col+1] == letter:
                    corners -= 1
            # three connected sides is two inverted corners
            if connected == 3:
                check_dir = []
                if not down:
                    check_dir.extend([(-1,-1), (-1,+1)])
                if not up:
                    check_dir.extend([(1,-1), (1,+1)])
                if not left:
                    check_dir.extend([(-1,+1), (1,+1)])
                if not right:
                    check_dir.extend([(-1,-1), (1,-1)])
                corners += 2

                for dx, dy in check_dir:
                    if arr[row+dx][col+dy] == letter:
                        corners -= 1
            # if there is only one connected side, we have two corners
            elif connected == 1:
                corners += 2
            # two connected sides not opposite is one corner
            # could be inside corners
            elif left + right == 1:
                if up + down == 1:
                    corners += 1
                    if (left and down):
                        if (arr[row+1][col-1] != letter):
                            corners += 1
                    if (left and up):
                        if (arr[row-1][col-1] != letter):
                            corners += 1
                    if (right and down):
                        if (arr[row+1][col+1] != letter):
                            corners += 1
                    if (right and up):
                        if (arr[row-1][col+1] != letter):
                            corners += 1

        return corners
    
    arr = []
    res = 0

    with open(filepath) as f:
        lines = [list(line.strip()) for line in f]
        arr = np.array(lines)
    
    visited = np.zeros((len(arr), len(arr[0])))
    regions = collections.defaultdict(list)

    # Traverse through the graph and create regions on areas not visited
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if visited[row][col]:
                continue
            visited[row][col] = 1
            letter = arr[row][col]
            new_region = bfs(arr, visited, letter, (row, col))
            regions[letter].append(new_region)
    
    # Calculate price
    for letter, region in regions.items():
        for sub_region in region:
            area = len(sub_region)
            if part2:
                sides = get_sides(arr, letter, sub_region)
                res += area * sides
            else:
                perimeter = get_perimeter(arr, letter, sub_region)
                res += area * perimeter

    return res

# assert day12('input_sample') == 1930
# assert day12('input') == 1483212
# assert day12('input_sample', part2=True) == 1206
print(day12('input', part2=True))
# time 0m0.331s