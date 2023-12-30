from functools import reduce
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(input):
    dirs = input[0]
    count = 0
    pos = [line[0:3] for line in input[2:] if line[2] == 'A']
    m = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in input[2:]}

    steps_needed = [0] * len(pos)
    to_solve = len(steps_needed)
    while to_solve > 0: 
        for i in range(len(pos)):
            pos[i] = m[pos[i]][dirs[count % len(dirs)]]
            if pos[i][2] == 'Z':
                steps_needed[i] = count + 1
                to_solve -=1
        count += 1
    return reduce(lcm, steps_needed, 1)

