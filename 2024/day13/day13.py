import re
import sys
import functools
import numpy as np

sys.setrecursionlimit(15000)
def day13(filepath, part2=False):
    @functools.lru_cache(maxsize=None)
    def recurse(target, da, db):
        if target == (0,0):
            return 0
        if target[0] < 0 or target[1] < 0:
            return sys.maxsize
        # press A
        tokens = min(3 + recurse((target[0]-da[0], target[1]-da[1]), da, db),
                        1 + recurse((target[0]-db[0], target[1]-db[1]), da, db))
        return tokens

    with open(filepath) as f:
        # read 3 lines
        A = (0,0)
        B = (0,0)
        target = (0,0)
        res = 0

        for line in f:
            if line.strip():
                match = re.search(r'(\d+)\D*(\d+)', line)
                if A == (0,0):
                    A = (int(match.group(1)), int(match.group(2)))
                elif B == (0,0):
                    B = (int(match.group(1)), int(match.group(2)))
                else:
                    target = (int(match.group(1)), int(match.group(2)))
                continue
            # new line found, execute logic
            if part2:
                target = [target[0]+10000000000000, target[1]+10000000000000]
            
            matrix = np.array([
                [A[0], B[0]],
                [A[1], B[1]]
            ])
            target = np.array([target[0], target[1]])
            
            a_press, b_press = np.linalg.solve(matrix, target)
            if np.array_equal(np.dot(matrix, (a_press.round(), b_press.round())), target):
                res += 3*a_press + b_press
            # i cant believe recursion didn't work
            # else:
            #     tokens = recurse(target, A, B)
            #     if tokens < sys.maxsize:
            #         res += tokens

            # reset data
            A = (0,0)
            B = (0,0)
            target = (0,0)

        return res

# assert day13('input_sample') == 480
print(day13('input', part2=True))
# time 0m0.214s