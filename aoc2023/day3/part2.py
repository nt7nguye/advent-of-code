
from curses.ascii import isdigit

def check(i, j, m, n):
    return 0 <= i < n and 0 <= j < m

def solve(lines):
    num = 0
    star_indexes = []
    n, m = len(lines), len(lines[0])
    star_index_to_num = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.isdigit():
                num = num * 10 + int(c)
                for di, dj in [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1)]:
                    if check(i + di, j + dj, m, n) and lines[i + di][j + dj] == '*':
                        if len(star_indexes) == 0 or star_indexes[-1] != (i + di, j + dj):
                            star_indexes.append((i + di, j + dj))
                            break
            
            if not c.isdigit() or j == m -1:
                if len(star_indexes):
                    for star_index in star_indexes:
                        star_index = '_'.join(str(star_index))
                        if star_index not in star_index_to_num:
                            star_index_to_num[star_index] = []
                        star_index_to_num[star_index].append(num)
                num = 0
                star_indexes = []

    s = 0
    for num_arr in star_index_to_num.values():
        if len(num_arr) == 2:
            s += num_arr[0] * num_arr[1]
    return s

