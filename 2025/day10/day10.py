from collections import deque
from scipy.optimize import linprog
import numpy as np

class Lights:
    def __init__(self, buttons):
        self.buttons = buttons

    def turn_on(self, goal):
        q = deque([(0,0)])
        while q:
            top, cnt = q.popleft()
            for button in self.buttons:
                new_top,new_cnt = cnt + 1, top ^ button
                if top == goal:
                    return cnt
                q.append((new_top, new_cnt))

        return -1

def parse_input(arr, part2=False):
    schematics = []
    all_buttons = []
    joltage = []
    for line in arr:
        buttons = []
        for word in line:
            if word[0] == '[' and word[-1] == ']':
                goal, size = parse_schematic(word[1:-1])
                schematics.append(goal)
            elif word[0] == '(' and word[-1] == ')':
                if part2:
                    buttons.append(list(map(int, word[1:-1].split(','))))
                else:
                    buttons.append(parse_button(word, size))

            else:
                joltage.append(parse_joltage(word))
        if part2:
            all_buttons.append(make_matrix(buttons, size))
        else:
            all_buttons.append(buttons)
    return schematics, all_buttons, joltage

def make_matrix(buttons, size):
    matrix = np.zeros((size, len(buttons)), dtype=int)
    for i, button in enumerate(buttons):
        for num in button:
            matrix[num][i] = 1
    return matrix

def parse_schematic(word):
    goal = 0
    for idx, c in enumerate(word):
        if c == '#':
            goal += 1 << len(word) - idx - 1
    return goal, len(word)

def parse_button(word, size, part2=False): 
    tup = list(map(int, word[1:-1].split(',')))
    result = sum(1 << (size - i - 1) for i in tup)
    return result            

def parse_joltage(word):
    return list(map(int, word[1:-1].split(',')))

def day10(filepath, part2=False):
    with open(filepath) as f:
        arr = [list(line.strip().split()) for line in f]
    
    schematics, buttons, joltage = parse_input(arr, part2)
    out = 0
    if part2:
        for i in range(len(buttons)):
            print(buttons[i])
            fun = linprog(np.ones(np.shape(buttons[i])[1]), A_eq=buttons[i], b_eq=joltage[i], integrality=1).fun
            out += fun
    else:
        for light, button in zip(schematics, buttons):
            l = Lights(button)
            out += l.turn_on(light)
    
    return out

print(day10('input_sample', part2=True))
print(day10('input', part2=True))