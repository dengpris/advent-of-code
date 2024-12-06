from collections import defaultdict

def day5(filepath, part2=False):
    # Create a tree: we can try to detect correct paths using cycles
    with open(filepath) as f:
        parsing = True
        tree = defaultdict(lambda: None)
        in_deg = defaultdict(int)
        top_order = []
        q = []
        cmp = []
        res = 0
        for line in f:
            # Build the graph and find topo sort
            if not line.strip():
                parsing = False
                continue
            # Parse the input
            if parsing:
                first, second = [int(x) for x in line.split('|')]
                if tree[first] is None:
                    tree[first] = [second]
                else:
                    tree[first].append(second)
                if tree[second] is None:
                    tree[second] = []
                cmp.append(line.strip())
            # Determine ordering
            else:
                arr = [int(x) for x in line.strip().split(',')]
                i,j = 0,1
                while j < len(arr):
                    if (tree[arr[i]] is None or arr[j] in tree[arr[i]]):
                        i += 1
                        j += 1
                    elif (tree[arr[j]] is None):
                        j += 1
                    elif arr[j] not in tree[arr[i]]:
                        if part2:
                            # ok whatever we brute force >:)
                            for x in range(len(arr)-1):
                                for y in range(len(arr)-x-1):
                                    if (f'{arr[y+1]}|{arr[y]}') in cmp:
                                        arr[y], arr[y+1] = arr[y+1], arr[y]
                            res += arr[(len(arr))//2]
                        break
                else:
                    if not part2:
                        res += arr[(len(arr))//2]
        #6567 too high
        return res
    
print(day5('input', part2=True))