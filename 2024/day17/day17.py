import re
import sys

class CPU:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.ip = 0
        self.res = []

    def get_out(self):
        return self.res
    
    def get_combo(self, num):
        if num <= 3:
            return num
        if num == 4:
            return self.A
        if num == 5:
            return self.B
        if num == 6:
            return self.C
        return None
    
    def adv(self, val):
        self.A >>= self.get_combo(val)

    def bxl(self, val):
        self.B ^= val

    def bst(self, val):
        self.B = self.get_combo(val) % 8

    def jnz(self, val):
        if self.A == 0:
            return
        self.ip = val - 2

    def bxc(self, val):
        self.B ^= self.C

    def out(self, val):
        # print(f'val: {val}, get_combo: {self.get_combo(val)}, ans: {self.get_combo(val) % 8}')
        self.res.append(self.get_combo(val) % 8)

    def bdv(self, val):
        self.B = self.A >> self.get_combo(val)

    def cdv(self, val):
        self.C = self.A >> self.get_combo(val)
    
    def do_op(self, op, val):
        match op:
            case 0:
                return self.adv(val)
            case 1:
                return self.bxl(val)
            case 2:
                return self.bst(val)
            case 3:
                return self.jnz(val)
            case 4:
                return self.bxc(val)
            case 5:
                return self.out(val)
            case 6:
                return self.bdv(val)
            case 7:
                return self.cdv(val)

    def run(self, ops):
        while self.ip < len(ops):
            # print(f'A: {self.A}, B: {self.B}, C: {self.C}')
            op = ops[self.ip]
            val = ops[self.ip + 1]
            self.do_op(op, val)
            self.ip += 2

def day17(filepath, part2=False):
    arr = []
    with open(filepath) as f:
        arr = f.readlines()
    
    if not part2:
        A = int(re.search(r'([\d]+)', arr[0]).group())
        B = int(re.search(r'([\d]+)', arr[1]).group())
        C = int(re.search(r'([\d]+)', arr[2]).group())
        ops = [int(x) for x in arr[-1].replace('Program: ', '').split(',')]
        cpu = CPU(A, B, C)
        
        cpu.run(ops)

        program = ','.join(map(str, cpu.get_out()))
        return program
    
    # 2,4,
    # 1,1,
    # 7,5,
    # 1,5,
    # 4,0,
    # 5,5,
    # 0,3,
    # 3,0
    # B = A % 8
    # B = B XOR 1
    # C = A >> B
    # B = B XOR 5
    # B = B XOR C
    # print B % 8 -> 0,4,1,7,6,4,1,0,2,7
    # A >> 3
    # Go to 0

    def recurse(idx, target, ops, curr):
        if idx >= len(target):
            return curr
        curr <<= 3
        for i in range(8):
            cpu_test = CPU(curr | i, 0, 0)
            cpu_test.run(ops)
            if cpu_test.get_out() == list(reversed(target[:idx+1])):
                a = recurse(idx+1, target, ops, curr | i)
                if a is not None:
                    return a
        return None


    if part2:
        target = [2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0]
        ops = target.copy()
        target.reverse()
        return recurse(0, target, ops, 0)


print(day17('input', part2=True))
# print(day17('input'))
# time: 0.212s