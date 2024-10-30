def day1(part1=True):
    with open('input') as op:
        res: int = 0
        for line in op:
            if part1:
                line = line.strip()
                i = 0
                j = len(line) - 1
                while True:
                    if (line[i].isnumeric()):
                        i = line[i]
                        break
                    i += 1
                while True:
                    if (line[j].isnumeric()):
                        j = line[j]
                        break
                    j -= 1

                res += int(i+j)

            else:
                str2num = {
                    'one': 1,
                    'two': 2,
                    'three': 3,
                    'four': 4,
                    'five': 5,
                    'six': 6,
                    'seven': 7,
                    'eight': 8,
                    'nine': 9
                }
                first = [99, 0] # [position, value]
                last = [-1 ,0] # [position, value]

                i = 0
                j = len(line) - 1
                while True:
                    if (line[i].isnumeric()):
                        first = i, int(line[i])
                        break
                    i += 1
                while True:
                    if (line[j].isnumeric()):
                        last = j, int(line[j])
                        break
                    j -=1

                for key in str2num:
                    pos = line.find(key)
                    rpos = line.rfind(key)
                    if pos == -1:
                        continue
                    if (pos < first[0]):
                        first = pos, str2num[key]
                    if (rpos > last[0]):
                        last = rpos, str2num[key]
                res += 10 * first[1] + last[1]
        
        return res

print(day1(part1=False))