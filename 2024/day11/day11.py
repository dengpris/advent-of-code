from functools import lru_cache 
def day11(filepath, part2=False):
    @lru_cache(maxsize=None)
    def recurse(x, blinks):
        if blinks == 0:
            return 1
        if x == 0:
            return recurse(1, blinks-1)
        if len(str(x)) % 2 == 0:
            mid = len(str(x)) // 2
            left_half, right_half = int(str(x)[:mid]), int(str(x)[mid:])
            return recurse(left_half, blinks-1) + recurse(right_half, blinks-1)
        return recurse(x * 2024, blinks-1)
    
    with open(filepath) as f:
        arr = [int(x) for x in f.read().split()]
        res = 0
        for x in arr:
            if part2:
                res += recurse(x, 75)
            else:
                res += recurse(x, 25)
        return res
    
# assert day11('input_sample') == 55312
print(day11('input', part2=True))
# time 0.302s