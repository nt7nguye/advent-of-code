def solve(input):
    int_map = {str(x): x for x in range(10)}
    s = 0
    for row in input:
        first = -1
        last = -1
        for char in row:
            if char in int_map:
                if first == -1:
                    first = int_map[char]
                    last = int_map[char]
                else:
                    last = int_map[char]
        s += first * 10 + last
    return s