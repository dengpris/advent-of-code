import re

def day3(filepath, part2=False):
    with open(filepath) as f:
        contents = f.read()
        en = 1
        res = 0
        reg_exp = 'mul\((\d{1,3})?,(\d{1,3})?\)'
        if part2:
            reg_exp = "mul\((\d{1,3})?,(\d{1,3})?\)|(do\(\))|(don't\(\))"

        arr = re.findall(reg_exp, contents)
        for pair in arr:
            if part2:
                if "do()" in pair:
                    en = 1
                elif "don't()" in pair:
                    en = 0
                elif en:
                    a, b, c, d = pair
                    res += int(a)*int(b)
            else:    
                a, b = pair
                res += int(a)*int(b)

        return res

print(day3('input', part2=True))