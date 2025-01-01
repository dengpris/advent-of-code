import collections

def day22(filepath, part2=False):
    class Secret:
        def __init__(self, num):
            self.num = num

        def get_num(self):
            return self.num
        
        def mix(self, val):
            self.num ^= val
        
        def prune(self):
            self.num %= 16777216
            
        def step(self, val):
            self.mix(val)
            self.prune()
            return self.get_num()

    with open(filepath) as f:
        arr = [int(line.strip()) for line in f]
    out = 0
    # dictionary with key: tuple and val: list
    # for each tuple we can sum the list and return the max
    # how long will this take?
    # update: did not take that long
    d = collections.defaultdict(list)
    for num in arr:
        flag = collections.defaultdict(bool)
        new_secret = Secret(num)
        seq = collections.deque([])
        diffs = collections.deque([])
        for it in range(2000):
            num = new_secret.step(num * 64)
            num = new_secret.step(num // 32)
            num = new_secret.step(num * 2048)
            dig = num % 10
            seq.append(dig)
            if it > 0:
                diffs.append(seq[-1] - seq[-2])
            if (len(seq) > 5):
                seq.popleft()
                diffs.popleft()
            tup = tuple(diffs)
            if (len(seq) == 5):
                if flag[tup] is False:
                    flag[tup] = True
                    d[tup].append(dig)
        out += num
    if part2:
        out = -1
        for val in d.values():
            if sum(val) > out:
                out = max(out, sum(val))
    return out

# assert day22('input_sample') == 37327623
print(day22('input', part2=True))
# time: 10.741s