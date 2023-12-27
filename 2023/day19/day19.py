import operator
operators = {
    '<': operator.lt,
    '>': operator.gt
}

def day19(filepath, part2=False):
    with open(filepath) as f:
        # parse input
        flag = 0
        workflows, instructions = {}, []
        for line in f:
            if not line.strip():
                flag = 1
                continue
            if not flag:
                # this is a workflow
                wkey, r = line.strip().split('{')
                rules = r.split(',')
                xmas = [] # three index list: operator (>, <), number (1234), and result
                for rule in rules:
                    if '}' in rule:
                        rule = rule[:-1]
                        xmas.append([-1, rule])
                        continue
                    # if ':' not in rule:
                    #     xmas[4].append()
                    cond, res = rule.split(':')
                    xmas.append([cond[0], cond[1], int(cond[2:]), res])
                print(f'{wkey}: {xmas}')
                workflows[wkey] = xmas.copy()
            else:
                instructions.append(line.strip()[1:-1])
    
    # lets start the workflow!
    print(instructions)
    accepted = 0
    rejected = 0
    for instruction in instructions:
        workflow = 'in'
        x, m, a, s = instruction.split(',')
        x = int(x[2:])
        m = int(m[2:])
        a = int(a[2:])
        s = int(s[2:])
        d = {
            'x': x,
            'm': m,
            'a': a,
            's': s
        }
        while workflow != 'A' or workflow != 'R':
            for cond in workflows[workflow]:
                letter = cond[0]
                if letter == -1:
                    workflow = cond[1]
                    continue
                if operators[cond[1]](d[letter], cond[2]):
                    workflow = cond[3]
                    break
            if workflow == 'A':
                print(f'{x}, {m}, {a}, {s}')
                accepted += x + m + a + s
                break
            if workflow == 'R':
                break
    return accepted
print(day19('input'))