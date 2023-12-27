with open('input') as op:
    memo = {}
    def recurse(cond: chr, records: str, n: int, cont: list, popped: bool) -> int:
        if n == len(records):
            if cont or cond == '#':
                return 0
            else:
                # print(records)
                return 1
        
        if not cont:
            if records[n:].count('#') > 0 or cond == '#':
                return 0
            else:
                # print(records)
                return 1
        
        new_cont = cont.copy()
        if records[n] == '.':
            if n > 0 and records[n-1] == '#' and not popped:
                return 0
            return recurse(cond, records, n+1, new_cont, False)
        
        if records[n] == '#':
            if popped:
                return 0
            if new_cont[0] == 1:
                new_cont.pop(0)
                popped = True
            else:
                new_cont[0] -= 1
                popped = False
            return recurse(cond, records, n+1, new_cont, popped)

        # if curr char is '?'
        # try replacing with #
        if cond == '#':
            if popped: # we cannot have consecutive #s if previous segment was removed
                return 0
            records = records[:n] + '#' + records[n+1:]
            if new_cont[0] == 1:
                new_cont.pop(0)
                popped = True
            else:
                new_cont[0] -= 1
                popped = False
        else:
            if n > 0 and records[n-1] == '#' and not popped:
                return 0
            records = records[:n] + '.' + records[n+1:]
            popped = False
        # print(records)
        # print(new_cont)

        arragement = recurse('#', records, n+1, new_cont, popped) + recurse('.', records, n+1, new_cont, popped)          
        return arragement

    out = 0
    for line in op:
        records, contiguous = line.strip().split()
        contiguous = list(map(int, contiguous.split(',')))

        p2_records = ""
        for i in range(5):
            p2_records += records + '?'
        p2_records = p2_records[:-1]
        contiguous = contiguous * 5
        print(p2_records)

        temp = recurse('#', p2_records, 0, contiguous, False) + recurse('.', p2_records, 0, contiguous, False)
        print(temp)
        out += temp
    print(out)