
def solve(input):
    s = 0
    max_value = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    for row in input:
        game_number = int(row.split(':')[0][5:])
        draws = row.split(':')[1].split(';')
        add = True
        for draw in draws:
            for val in draw.split(','):
                _, num, color = val.split(' ')
                if int(num) > max_value[color]:
                    add = False
        if add:
            s += game_number
    return s