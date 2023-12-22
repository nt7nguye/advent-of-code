
def solve(input):
    time = [int(num) for num in input[0].split()[1:]]
    distance = [int(num) for num in input[1].split()[1:]]
    n = len(time)
    ans = 1
    for i in range(n):
        t = time[i]
        d = distance[i]
        beat = 0
        for i in range(t):
            total_dist = (t - i) * i
            beat += 1 if total_dist > d else 0
        ans *= beat
    return ans
