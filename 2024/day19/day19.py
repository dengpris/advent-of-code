from functools import cache

global towels
def day19(filepath, part2=False):
    @cache
    def recurse(curr, target, part2=False):
        if (len(curr) > len(target)):
            return 0
        
        if (curr == target):
            return 1
        
        out = 0
        for towel in towels:
            take = curr + towel
            if take == target[:len(take)]:
                if part2:
                    out += recurse(take, target, True)
                else:
                    if recurse(take, target):
                        return 1
        return out
        # return out
            
    with open(filepath) as f:
        arr = f.readlines()
    towels = arr[0].strip().split(', ')
    patterns = [line.strip() for line in arr[2:]]

    res = 0
    for pattern in patterns:
        res += recurse('', pattern, part2=part2)

    return res

assert day19('input_sample') == 6
print(day19('input', part2=True))
# time: 1.892s