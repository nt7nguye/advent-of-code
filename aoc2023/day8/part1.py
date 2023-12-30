
def solve(input):
    dirs = input[0]
    count = 0
    pos = 'AAA'
    m = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in input[2:]}
    
    while pos != 'ZZZ':
        pos = m[pos][dirs[count % len(dirs)]]
        count += 1

    return count

