
def day7(filepath, part2=False):
    def concat(x, y):
        return int(str(x)+str(y))

    def combination_ops(lhs, rhs, idx, curr, part2=False):
        if idx == len(rhs):
            if curr == lhs:
                return 1
            return 0
        
        if curr > lhs:
            return 0
        
        ans = (combination_ops(lhs, rhs, idx+1, rhs[idx] + curr, part2) or 
                combination_ops(lhs, rhs, idx+1, rhs[idx] * curr, part2))
        
        if part2:
            ans = ans or combination_ops(lhs, rhs, idx+1, concat(curr, rhs[idx]), part2)

        return ans

    
    with open(filepath) as f:
        res = 0
        for line in f:
            lhs, *rhs = [int(x) for x in line.replace(':', '').split()]
            # recursion
            if combination_ops(lhs, rhs, 0, 0, part2=part2):
                res += lhs
        return res

print(day7('input', part2=True))
# time: 4.854s