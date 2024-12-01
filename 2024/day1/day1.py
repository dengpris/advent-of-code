import collections

def day1(filepath, part2=False):
    with open(filepath) as f:
        l_arr = []
        r_arr = []
        for line in f:
            l, r = line.split()
            l_arr.append(int(l))
            r_arr.append(int(r))

        res = 0
        
        if (part2):
            l_dict = collections.defaultdict(int)
            r_dict = collections.defaultdict(int)
            for l, r in zip(l_arr, r_arr):
                l_dict[l] += 1
                r_dict[r] += 1
            for key in l_dict.keys():
                res += key * l_dict[key] * r_dict[key]
        
        else:
            l_arr.sort()
            r_arr.sort()

            for l, r in zip(l_arr, r_arr):
                res += abs(l-r)
        
        return res

print(day1('input', part2=True))