
def shortest_path(input, pos_1, pos_2, expand_rows, expand_cols):
    steps = 0
    start, end = min(pos_1[0], pos_2[0]), max(pos_1[0], pos_2[0])
    steps += end - start
    for i in range(start + 1, end):
        if i in expand_rows:
            steps += 999999
    
    start, end = min(pos_1[1], pos_2[1]), max(pos_1[1], pos_2[1])
    steps += end - start
    for i in range(start + 1, end):
        if i in expand_cols:
            steps += 999999
    return steps

def solve(input):
    total = 0
    n = len(input)
    m = len(input[0])
    expand_rows = set([i for i in range(n) if all([input[i][j] == '.' for j in range(m)])])
    expand_cols = set([j for j in range(m) if all([input[i][j] == '.' for i in range(n)])])
    galaxies = [(i, j) for i in range(n) for j in range(m) if input[i][j] == '#']
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            total += shortest_path(input, galaxies[i], galaxies[j], expand_rows, expand_cols)
    return total