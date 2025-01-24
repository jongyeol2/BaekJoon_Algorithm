import math

def solution(arr):
    while True:
        if math.log2(len(arr)).is_integer():
            break
        arr.append(0)
    return arr