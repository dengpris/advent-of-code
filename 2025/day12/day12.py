def parse_input(arr):
    shapes = []
    dims = []
    counts = []

    for line in arr:
        if line.strip().endswith(":"):
            shapes.append(0)

        elif "#" in line:
            shapes[-1] += line.count("#")

        elif "x" in line:
            all_dims, all_counts = line.split(":")
            dims.append([int(dim) for dim in all_dims.split('x')])
            counts.append([int(count) for count in all_counts.split()])

    return shapes, dims, counts

def day12(filepath, part2=False):
    with open(filepath) as f:
        arr = f.read().splitlines()
    
    res = 0
    shapes, dims, counts = parse_input(arr)

    for idx in range(len(counts)):
        width, height = dims[idx]
        count = counts[idx]
        area = sum(num * shapes[i] for i, num in enumerate(count))

        if area <= width * height:
            res += 1
    
    return res

print(day12('input'))