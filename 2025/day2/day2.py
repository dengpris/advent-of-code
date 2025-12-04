
def get_invalid(r_start: str, r_end: str, part2=False) -> list[int]:
    start = int(r_start)
    end = int(r_end)
    out = []

    while start <= end:
        start_str = str(start)
        length = len(start_str)
        if part2 and length > 1:
            for step in range(1, (length + 1) // 2 + 1): # ceiling
                if check_invalid(0, step, "", start_str):
                    print(f"found a valid: {start}")
                    out.append(start)
                    break
        else:
            if length % 2:
                start = pow(10, length) # add 0 and reset to exp(10)
                continue
            # Check if first half == second half
            upper, lower = start_str[:length // 2], start_str[length // 2:]
            if upper == lower:
                out.append(start)
        
        start += 1

    return out

# Check if split string is valid using recursion
def check_invalid(start, end, substr, string):
    # Return early if step does not evenly split
    if (len(string) % (end - start)):
        return False
    # Base condition
    if end > len(string):
        return True
    # Start condition
    if (start == 0):
        return check_invalid(end, end + (end-start), string[:end], string)
    # Fail condition
    if string[start:end] != substr:
        return False
    # Recursion
    return check_invalid(end, end + len(substr), substr, string)


def day2(filepath, part2=False):
    with open(filepath) as f:
        ranges = f.read().split(',')
        out = 0
        for r in ranges:
            r_start, r_end = r.split('-')
            out += sum(get_invalid(r_start, r_end, part2))
        print(out)
        return out
    
assert day2('input_sample', part2=False) == 1227775554
assert day2('input_sample2', part2=False) == 1010
# print(day2('input', part2=False))

assert day2('input_sample2', part2=True) == 2009
assert day2('input_sample', part2=True) == 4174379265
print(day2('input', part2=True))