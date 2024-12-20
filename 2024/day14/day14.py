import collections
def day14(filepath, part2=False):
    def find_quandrant(px, py, wall_width, wall_height):
        mid_w = wall_width // 2
        mid_h = wall_height // 2
        if (px == mid_w) or (py == mid_h):
            return 0
        
        if (px < mid_w):
            if (py < mid_h):
                return 1
            else:
                return 2
        else:
            if (py < mid_h):
                return 3
            else:
                return 4

    with open(filepath) as f:
        wall_width = 101
        wall_height = 103
        quandrants = collections.defaultdict(int)
        seconds = 0          
        arr = []
        for line in f:
            p, v = line.split()
            p = p.replace('p=', '')
            px, py = [int(x) for x in p.split(',')]
            v = v.replace('v=', '')
            vx, vy = [int(x) for x in v.split(',')]

            arr.append([(px, py), (vx, vy)])
        
        while True:
            picture = [['.' for i in range(wall_width)] for j in range(wall_height)]
            seconds += 1
            for a in arr:
                px, py = a[0]
                vx, vy = a[1]

                if not part2:
                    px = (px + 100 * vx) % wall_width 
                    py = (py + 100 * vy) % wall_height 

                    q = find_quandrant(px, py, wall_width, wall_height)
                    if q:
                        quandrants[q] += 1
                else:
                    px = (px + seconds * vx) % wall_width
                    py = (py + seconds * vy) % wall_height
                    picture[py][px] = '#'

            if not part2:
                res = 1
                for val in quandrants.values():
                    res *= val
                return res
            
            for i in range(wall_height):
                row = (''.join(picture[i]))
                if '###########' in row:
                    return seconds

# assert day14('input') == 209409792
print(day14('input', part2=True))
# time 1.630s