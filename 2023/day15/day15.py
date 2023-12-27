with open('input') as f:
    for line in f:
        hash_input = line.strip()
    
    def hash_algo(string):
        curr = 0
        for c in string:
            curr += ord(c)
            curr *= 17
            curr %= 256
        return curr

    sequences = [i for i in hash_input.split(',')]
    boxes = dict()
    lens = dict()
    
    for op in sequences:
        if op[-1] == '-':
            label = op[:-1]
            n = hash_algo(label)
            if n not in boxes:
                continue
            if label in boxes[n]:
                boxes[n].remove(label)
        else:
            focal = int(op[-1])
            label = op[:-2]
            n = hash_algo(label)
            if n not in boxes:
                boxes[n] = []
            if label not in boxes[n]:
                boxes[n].append(label)
            lens[label] = focal
    
    out = 0
    for key, val in boxes.items():
        for slot, item in enumerate(val):
           out += (key + 1) * (slot + 1) * lens[item] 
            
    print(out)