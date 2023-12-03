
from curses.ascii import isdigit

def check(i, j, m, n):
    return 0 <= i < n and 0 <= j < m

def solve(lines):
    s = 0
    num = 0
    f = True
    n, m = len(lines), len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.isdigit():
                num = num * 10 + int(c)
                for di, dj in [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1)]:
                    if check(i + di, j + dj, m, n) and lines[i + di][j + dj] not in '0123456789.':
                        f = True
                        break
            
            if not c.isdigit() or j == m -1:
                if f:
                    s += num
                num = 0
                f = False
            
    return s

