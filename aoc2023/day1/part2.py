
from re import X


def solve(input):
    number_map = {str(x): x for x in range(10)}
    number_map = {**number_map, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    s = 0
    for row in input:
        first, last = -1, -1
        for i in range(len(row)):
            num = -1 if row[i] not in number_map else number_map[row[i]]
            for j in range(3, 6):
                if i+j <= len(row) and row[i:i+j] in number_map:
                    num = number_map[row[i:i+j]]
                    break
            if num != -1:
                if first == -1:
                    first = num
                last = num
        s += first * 10 + last
    return s