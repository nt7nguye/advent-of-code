
pos_map = {
    'F': [(1, 0), (0, 1)],
    '-': [(0, -1), (0, 1)],
    '7': [(0, -1), (1, 0)],
    '|': [(-1, 0), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    'L': [(0, 1), (-1, 0)],
    '.': 
}

def find_start(input, n, m):
    for i in range(n):
        for j in range(m):
            if input[i][j] == 'S':
                return i, j

def valid(i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m

def loop_length(input, i, j, n, m):
    count = 1
    while input[i][j] != 'S':
        for offsets in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_i, next_j = i + offsets[0], j + offsets[1]
            if valid(next_i, next_j, n, m):
                if 
                pipe = input[next_i, next_j]
                if pos_map[pipe][0] == (-offsets[0], -offsets[1]):
                    start = (start[0] + offsets[0], start[1] + offsets[1])
                    break
                elif pos_map[pipe][1] == (-offsets[0], -offsets[1]):
                    start = (start[0] + offsets[0], start[1] + offsets[1])
                    break
                else:

        count += 1
    return count
            
    

def solve(input) -> None:
    n, m = len(input), len(input[0])
    start = find_start(input, n, m)
    return 
        
