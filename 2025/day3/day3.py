def get_max_joltage(batteries: list[int]) -> int:
    res: int = 0
    tens_dig, ones_dig = -1, -1
    for power in batteries:
        if power > ones_dig:
            ones_dig = power
            res = max(res, tens_dig * 10 + ones_dig)
        if power > tens_dig:
            tens_dig = power
            ones_dig = -1

    print(f'res is {res}')
    return res

def get_max_j_p2(batteries: list[int]) -> int:
    # Use last 12 digits, then work backwords (greedy)
    left_stop: int = 0
    res = 0
    for i in range(len(batteries)-12, len(batteries)):
        idx: int = i
        max_dig = batteries[i]
        while (idx >= left_stop):
            if batteries[idx] >= max_dig:
                max_dig = batteries[idx]
                curr_idx = idx
            idx -= 1
        res = 10 * res + max_dig
        left_stop = curr_idx + 1
    print(f'res is {res}')
    return res

def day3(filepath, part2=False):
    with open(filepath) as f:
        joltage = 0
        for lines in f:
            banks = [int(c) for c in list(lines.strip())]
            if not part2:
                joltage += get_max_joltage(banks)
            else:
                joltage += get_max_j_p2(banks)

    return joltage

assert day3('input_sample', part2=False) == 357
assert day3('input_sample', part2=True) == 3121910778619
print(day3('input', part2=True))
