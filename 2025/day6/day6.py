import math

def get_vertical_nums(nums, idx):
    constructed_nums = []

    while idx < len(max(nums, key=len)):
        constructed = 0
        for row in nums:
            if idx >= len(row):
                continue
            if row[idx].isnumeric():
                dig = int(row[idx])
                constructed = constructed * 10 + dig
        
        if constructed == 0: # Space found
            break
        # Add vertical number to array    
        constructed_nums.append(constructed)
        idx += 1
    # Return array and new index
    return constructed_nums, idx + 1
        

def day6(filepath, part2=False):
    # Setup
    with open(filepath) as f:
        lines = f.readlines()
        if not part2:
            nums = [line.strip().split() for line in lines[:-1]]
        else:
            nums = [line.rstrip() for line in lines[:-1]]
        operations = lines[-1].strip().split()
    # Logic
    res = 0
    if not part2:
        for i in range(len(operations)):
            if operations[i] == '+':
                res += sum([int(arr[i]) for arr in nums])
            else:
                res += math.prod([int(arr[i]) for arr in nums])
    else:
        idx = 0 # Index of string
        i = 0 # Index of operation
        while idx < len(nums[0]):
            constructed_nums, idx = get_vertical_nums(nums, idx)
            if operations[i] == '+':
                res += sum(constructed_nums)
            else:
                res += math.prod(constructed_nums)
            i += 1
        
    return res

assert day6('input_sample', part2=False) == 4277556
assert day6('input_sample', part2=True) == 3263827
print(day6('input', part2=True))
