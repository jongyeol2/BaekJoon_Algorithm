def solution(arr):
    row = len(arr)
    col = len(arr[0])
    size = max(row, col)
    
    for i in range(row):
        arr[i] += [0] * (size - col)
    
    for _ in range(size - row):
        arr.append([0] * size)
    
    return arr