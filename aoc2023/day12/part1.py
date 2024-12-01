
def permutations(line, start, end, groups):
    if len(groups) == 0:
        return 0
    if start == 

def solve(input):
    total = 0
    for line in input:
        start = end = -1
        for i, char in enumerate(line):
            if char == '?':
                end = i
                start = i if start != -1
