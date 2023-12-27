import functools
with open('input') as op:
    memo = {}
    @functools.cache
    def recurse(records: str, cont: tuple) -> int:
        if not len(records):
            if cont:
                return 0
            else:
                return 1
        
        if not cont:
            if records.count('#') > 0:
                return 0
            else:
                return 1
        
        if records[0] == '.':
            return recurse(records[1:], cont)
        
        new_cont = cont
        if records[0] == '#':
            if len(records) < cont[0]:
                return 0
            temp = records[:cont[0]]
            if temp.replace('?', '#') != cont[0] * '#':
                return 0
            else:
                if len(records) == cont[0]:
                    if len(cont) == 1:
                        return 1
                    else:
                        return 0
                if records[cont[0]] == '#':
                    return 0
                new_cont = cont[1:]
                return recurse(records[cont[0]+1:], new_cont)

        if records[0] == '?':
            ret = recurse(records[1:], cont)
            if len(records) < cont[0]:
                return ret            
            temp = records[:cont[0]]
            if temp.replace('?', '#') != cont[0] * '#':
                return ret
            else:
                if len(records) < cont[0]:
                    return ret
                if len(records) == cont[0]:
                    if len(cont) == 1:
                        return ret + 1
                    else:
                        return ret
                if len(records) > cont[0] and records[cont[0]] == '#':
                    return ret
                new_cont = cont[1:]
                return ret + recurse(records[cont[0]+1:], new_cont)
        raise Exception
    
    out = 0
    for line in op:
        records, contiguous = line.strip().split()
        contiguous = list(map(int, contiguous.split(',')))

        p2_records = ""
        for i in range(5):
            p2_records += records + '?'
        p2_records = p2_records[:-1]
        contiguous = contiguous * 5
        contiguous = tuple(contiguous)

        temp = recurse(p2_records, contiguous)
        print(temp)
        out += temp
    print(out)