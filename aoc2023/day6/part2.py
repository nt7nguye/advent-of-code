
def solve(input):
    time = int(''.join(input[0].split()[1:]))
    distance = int(''.join(input[1].split()[1:]))
    beat = 0
    for i in range(time):
        total_dist = (time - i) * i
        beat += 1 if total_dist > distance else 0
    return beat
