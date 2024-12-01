
def predict(arr): 
    stacked_arr = [arr]
    stacked_idx = 0
    while any([num != 0 for num in arr]):
        next_arr = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        stacked_idx += 1
        stacked_arr.append(next_arr)
        arr = next_arr
    
    diff = 0
    for idx in range(stacked_idx - 1, -1, -1):
        diff = stacked_arr[idx][0] - diff
    return diff 

def solve(input):
    total = 0
    for line in input:
        num = predict([int(num) for num in line.split(' ')])
        total += num
    return total
