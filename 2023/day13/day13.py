from math import ceil

with open('input') as op:
    def check_reflect(middle, m):
        if middle < len(m) / 2:
            start = 0
        else:
            start = 2 * middle - len(m)
        end = middle * 2 - 1
        smudge = 0
        for i in range(start, middle):
            for j in range(len(m[i])):
                if (m[i][j] != m[end - i][j]):
                    smudge += 1
                    if smudge > 1:
                        return False
        if not smudge:
            return False
        return True

    out = 0
    m = []
    for line in op:
        if len(line.strip()):
            m.append(list(map(str, line.strip())))
            continue
        # print(m)
        m_transpose = list(zip(*m))
        for i in range(1, len(m)):
            if check_reflect(i, m):
                out += i * 100
                break
        
        for i in range(1, len(m_transpose)):
            if check_reflect(i, m_transpose):
                out += i
                break
        m = []
    
    print(out)