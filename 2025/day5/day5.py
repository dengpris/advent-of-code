import bisect

class FreshIDs:
    def __init__(self, arr):
        self.fresh_ranges = []
        self.combine_ranges(arr)

    def combine_ranges(self, arr):
        arr.sort()
        start, end = arr[0][0], arr[0][1]
        for lower, upper in arr[1:]:
            if lower <= end:
                end = max(end, upper)
            else:
                self.fresh_ranges.append((start, end))
                start, end = lower, upper

        self.fresh_ranges.append((start, end))

    def check_fresh(self, fruitId):
        pos = bisect.bisect_left(self.fresh_ranges, fruitId, key=lambda x: x[0])
        # print(f"my id is {fruitId}")

        if pos == len(self.fresh_ranges):
            if self.fresh_ranges[-1][1] >= fruitId:
                return True
        elif self.fresh_ranges[pos][0] == fruitId:
                return True
        elif pos and self.fresh_ranges[pos-1][1] >= fruitId:
                return True
        return False

def day5(filepath, part2=False):
    with open(filepath) as f:
        ids = []
        ranges = []
        for line in f:
            if not len(line.strip()):
                continue
            try:
                start, end = map(int, line.strip().split('-'))
                ranges.append((start, end))
            except:
                ids.append(int(line.strip()))
        f = FreshIDs(ranges)

        out = 0
        if part2:
            for start, end in f.fresh_ranges:
                out += (end - start + 1)
            return out
        
        for i in ids:
            out += f.check_fresh(i)

        return out

assert day5('input_sample') == 3 
print(day5('input', part2=True))