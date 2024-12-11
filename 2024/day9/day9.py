import bisect
import collections

def day9(filepath, part2=False) -> int:
    input = ""
    with open(filepath) as f:
        input = f.readlines()[0].strip()

    filestring = []
    id, is_free_space = 0, 0
    res = 0

    if part2:
        # let's keep track of all the positions of emtpies and files
        idx = 0
        empty = [] # (size, idx)
        full = [] # (id, size, idx) don't get mixed up!
        for x in input:
            x = int(x)
            if is_free_space:
                bisect.insort_left(empty, (idx, x))
            else:
                bisect.insort_left(full, (id, idx, x))
                id += 1
            idx += x
            is_free_space = not is_free_space

        # iterate backwards through full - continue until?
        full.reverse()
        for id, idx, sz, in full:
            pos = 0
            # where is the first elibile empty space?
            while pos < len(empty):
                if empty[pos][1] >= sz:
                    break
                pos += 1
            if pos >= len(empty) or empty[pos][0] >= idx: # does not fit or will move farther down
                # add directly to answer
                for i in range(sz):
                    res += (idx + i) * id
                continue
            # fill in empty
            old_idx, old_size = empty[pos]
            new_size = old_size - sz;
            new_idx = old_idx + sz
            del(empty[pos])
            if new_size > 0:
                bisect.insort_left(empty, (new_idx, new_size))
            for i in range(sz):
                res += (old_idx + i) * id

    else:
        for x in input:
            x = int(x)
            if is_free_space:
                filestring.extend([-1]*x)
            else:
                filestring.extend([id]*x)
                id += 1
            is_free_space = not is_free_space
        # two pointer solution
        i, j = 0, len(filestring)-1
        while (i < j):
            # i is the latest free space idx
            while (i < len(filestring) and filestring[i] != -1):
                i += 1
            # j is the latest non-free space to be moved
            while (j >= 0 and filestring[j] == -1):
                j -= 1
            
            if (i >= j):
                break

            filestring[i] = filestring[j]
            filestring[j] = -1
            i += 1
            j -= 1
        
        for i, num in enumerate(filestring):
            if num == -1:
                break
            res += i * num
    return res
        
# assert day9('input_sample') == 1928
# assert day9('input') == 6242766523059
# assert day9('input_sample', part2=True) == 2858
print(day9('input', part2=True))
# time: 0.340s