import numpy as np
with open('input') as op:
    def calculate_load(m):
        # # m_transpose = list(zip(*m))
        # m = np.rot90(m)
        out = 0
        size = len(m)
        for i, row in enumerate(m):
            for col in row:
                if col == 'O':
                    out += size - i
        # for col in m:
        #     empty_space = []
        #     for j, item in enumerate(col):
        #         if item == '.':
        #             empty_space.append(size - j)
        #         elif item == 'O':
        #             if not empty_space:
        #                 out += size - j
        #             else:
        #                 out += empty_space[0]
        #                 empty_space = empty_space[1:]
        #                 empty_space.append(size - j)
        #         elif item == '#':
        #             empty_space = []
        return out
                    
    def rotate(m, cycles):
        m_rotate = m.copy()
        m_rotate = np.rot90(m_rotate, 2)
        for _ in range(cycles):     
            # north west south east -> rotate 1, 0, 3, 2
            for i in range(4):
                m_rotate = np.rot90(m_rotate, k=-1)
                for col in m_rotate:
                    empty_space = []
                    for j, item in enumerate(col):
                        if item == '.':
                            empty_space.append(j)
                        elif item == 'O':
                            if empty_space:
                                col[empty_space[0]] = 'O'
                                col[j] = '.'
                                empty_space = empty_space[1:]
                                empty_space.append(j)
                        elif item == '#':
                            empty_space = []
                # m_rotate = np.rot90(m_rotate, 4 - i)
        m_rotate = np.rot90(m_rotate, 2)
        # for _ in np.rot90(m_rotate, 3):
        #     print(_)
        return m_rotate
    
    m = []
    for line in op:
        m.append(list(map(str, line.strip())))
    
    m = np.array(m)
    out = []
    m = rotate(m, 2000)
    for i in range(50):
        m = rotate(m, 1)
        out.append(calculate_load(m))
    print(out)
        
