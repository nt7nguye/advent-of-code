

def solve(input):
    card_instances = [1] * 186
    for i, line in enumerate(input):
        tokens = line.split(' ')
        winning = set()
        checking = False
        point = 0
        for token in tokens[2:]:
            if token == '':
                continue
            elif token == '|':
                checking = True
            elif checking:
                point += token in winning
            else:
                winning.add(token)
        for j in range(i + 1, min(186, i + 1 + point)):
            card_instances[j] += card_instances[i]
    return sum(card_instances)