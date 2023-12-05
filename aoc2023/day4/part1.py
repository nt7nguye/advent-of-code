
def solve(input):
    total = 0
    for line in input:
        tokens = line.split(' ')
        winning = set()
        checking = False
        point = 0.5
        for token in tokens[2:]:
            if token == '':
                continue
            elif token == '|':
                checking = True
            elif checking:
                if token in winning:
                    point *= 2
            else:
                winning.add(token)
        total += point if point != 0.5 else 0
    return total