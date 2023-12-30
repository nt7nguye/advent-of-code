
def predict(arr): 
    stacked_arr = [arr]
    stacked_idx = 0
    while any([num != 0 for num in arr]):
        next_arr = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        stacked_idx += 1
        stacked_arr.append(next_arr)
        arr = next_arr
    
    stacked_arr[stacked_idx].append(0)
    stacked_idx -= 1
    while stacked_idx > -1:
        stacked_arr[stacked_idx].append(
            stacked_arr[stacked_idx + 1][-1] +
            stacked_arr[stacked_idx][-1]
        )
        stacked_idx -= 1
    return stacked_arr[0][-1]

def solve(input):
    total = 0
    for line in input:
        num = predict([int(num) for num in line.split(' ')])
        total += num
    return total
