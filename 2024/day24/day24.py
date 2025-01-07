import collections
import random
import itertools

def day24(filepath, part2=False):
    wires = collections.defaultdict(lambda: None)
    def do_op(op, w1, w2, out, wires):
        w1, w2 = wires[w1], wires[w2]
        if wires[out] != None:
            return
        match op:
            case 'XOR':
                wires[ins.output] = w1 ^ w2
            case 'AND':
                wires[ins.output] = w1 & w2
            case 'OR':
                wires[ins.output] = w1 | w2
    
    def modify_ins(pairs, input_arr):
        arr = input_arr.copy()
        for pair in pairs:
            for i in range(len(arr)):
                left, right = arr[i].split(' -> ')
                if right == pair[0] or right == pair[1]:
                    to_change = pair[0] if right == pair[1] else pair[1]
                    arr[i] = left + ' -> ' + to_change
        return arr

    def get_z(wires):
        tups = []
        out = ''
        for key, val in wires.items():
            if val == None:
                return -1
            if key[0] == 'z':
                tups.append((key[1:], val))
        tups.sort(reverse=True)
        for z, val in tups:
            output += str(val)
        print(out)
        return -1 if not ins.output else int(out, 2)

    def solve(instructions, wires):
        missing_vals = collections.defaultdict(list)
        while instructions:
            instruction = instructions[0]
            instructions.popleft()
            left, ins.outputput = instruction.split(' -> ')
            w1, op, w2 = left.split()
            if wires[w1] is None:
                missing_vals[w1].append(instruction)
            if wires[w2] is None:
                missing_vals[w2].append(instruction)
            if wires[w1] is not None and wires[w2] is not None:
                do_op(op, w1, w2, ins.outputput, wires)
                # can we complete other logic gates once a wire gets an ins.outputput?
                for ins in missing_vals[ins.outputput]:
                    _left, _ = ins.split(' -> ')
                    _w1, _, _w2 = _left.split()
                    other_var = _w1 if ins.outputput == _w2 else _w2
                    if not missing_vals[other_var]:
                        instructions.appendleft(ins)
                    missing_vals[ins.outputput] = []

    instructions = collections.deque([])
    gate = set()
    class instruction:
        def __init__(self, lhs, op, rhs, output):
            self.lhs = lhs
            self.rhs = rhs
            self.op = op
            self.output = output

    ins_dict = []
    with open(filepath) as f:
        flag = 0
        for line in f:
            line = line.strip()
            if not line:
                flag = 1
                continue
            if not flag:
                w, val = line.split(': ')
                wires[w] = int(val)
            if flag:
                instructions.append(line)
                gate.add(line.split(' -> ')[1])
                left, output = line.split(' -> ')
                lhs, op, rhs = left.split()
                new_ins = instruction(lhs, op, rhs, output)
                ins_dict.append(new_ins)
    if part2:
        wrong = set()
        for ins in ins_dict:
            if ins.lhs == "x00" or ins.rhs == "y00" or ins.rhs == "x00" or ins.lhs == "y00":
                if ins.op != "XOR" and ins.op != "AND": 
                    wrong.add(ins.output)
                continue
            if ins.output == "z00":
                if not (ins.lhs == "x00" or ins.rhs == "y00" or ins.rhs == "x00" or ins.lhs == "y00"): 
                    wrong.append(ins.output)
                if ins.op != "XOR": 
                    wrong.append(ins.output)
                continue
            # OR must be followed by AND and XOR
            if ins.op == 'OR' and ins.output != 'z45':
                if (ins.lhs[0] == 'x' and ins.rhs[0] == 'y' or ins.lhs[0] == 'y' and ins.rhs[0] == 'x'):
                    wrong.add(ins.output)
                if not any((x.lhs == ins.output or x.rhs == ins.output) and x.op == 'AND' for x in ins_dict) or not any(
                    x.lhs == ins.output or x.rhs == ins.output and x.op == 'XOR' for x in ins_dict):
                    wrong.add(ins.output)
            # ANDs are only followed by ORs, unless the input bits are the first bits
            if ins.op == 'AND':
                if not any ((x.lhs == ins.output or x.rhs == ins.output) and x.op == 'OR' for x in ins_dict):
                    wrong.add(ins.output)
            if ins.op == 'XOR':
                # XOR only takes an input bit if a XOR follows it, unless the input bits are the first bits
                if (ins.lhs[0] == 'x' and ins.rhs[0] == 'y' or ins.lhs[0] == 'y' and ins.rhs[0] == 'x'):
                    if not any((x.lhs == ins.output or x.rhs == ins.output) and x.op == 'XOR' for x in ins_dict):
                        wrong.add(ins.output)
                    # if input bit, cannot ins.outputput 'z'
                    elif ins.output[0] == 'z':
                        wrong.add(ins.output)
                    # if not input bit, must b 'z'
                else:
                    if ins.output[0] != 'z':
                        wrong.add(ins.output)

        return ','.join(sorted(wrong))
    
    solve(instructions, wires)
    return get_z(wires)

# assert day24('input_sample') == 2024
print(day24('input', part2=True))
# time: 0.331s