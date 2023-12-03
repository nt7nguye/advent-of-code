
def solve(input):
    s = 0
    for row in input:
        draws = row.split(':')[1].split(';')
        max_draw = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for draw in draws:
            for val in draw.split(','):
                _, num, color = val.split(' ')
                if int(num) > max_draw[color]:
                    max_draw[color] = int(num)
        s += max_draw['red'] * max_draw['green'] * max_draw['blue']
    return s