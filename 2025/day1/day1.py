from enum import Enum

class Dir(Enum):
    L = -1
    R = 1


class Dial:
    def __init__(self, val):
        self.value: int = val

    def __add__(self, x):
        self.value = (self.value + x) % 100
        return self.value
    
    def parse(self, s: str):
        return Dir[s[:1]], int(s[1:])

    def rotate(self, s):
        d, steps = self.parse(s)

        # Part 2 logic start
        quot, rem = divmod(steps, 100)
        quot = abs(quot)
        after = self.value + d.value * rem # Final turn
        if self.value != 0 and (after > 99 or after <= 0):
            quot += 1
        # Part 2 logic end

        self.__add__(d.value * steps)
        return quot

    
    
def day1(filepath, part2=False):
    with open(filepath) as f:
        dial = Dial(50)
        val = 0
        for line in f: 
            if not part2:
                if dial.rotate(line.strip()) == 0:
                    val += 1
            else:
                val += dial.rotate(line.strip())
        print("final answer is: ", val)
        return val
    
assert day1('input_sample', part2=True) == 6
assert day1('input_sample2',part2=True) == 2

print(day1('input', part2=True))